################################################################################
#
# Copyright (c) 2017, DbgVis - The Debugger Visualizer
# Copyright (c) 2017, Peter Andreas Entschev
# All rights reserved.
#
# BSD 3-Clause License
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
################################################################################

import gdb
import numpy as np
from DbgVis import Visualizer
from DbgVis import DebuggerInterface

class PyCVMat():
    """Python cv::Mat-like container"""

    openCVMagicVal = 0x42ff0000
    openCVMagicValMask = 0xffff0000
    openCVMaxChannels = 512
    openCVMaxDepth = 7
    openCVDepthBits = 3
    openCVTypeNames = { 0: 'CV_8U',
                        1: 'CV_8S',
                        2: 'CV_16U',
                        3: 'CV_16S',
                        4: 'CV_32S',
                        5: 'CV_32F',
                        6: 'CV_64F',
                        7: 'CV_USRTYPE1' }
    openCVTypeSizes = { 'CV_8U': 1,
                        'CV_8S': 1,
                        'CV_16U': 2,
                        'CV_16S': 2,
                        'CV_32S': 4,
                        'CV_32F': 4,
                        'CV_64F': 8,
                        'CV_USRTYPE1': 0 }

    def __init__(self, obj):
        # cv::Mat's attributes
        self.rows = obj['rows']
        self.cols = obj['cols']
        self.step = obj['step']['buf'][0]
        self.flags = obj['flags']
        self.data = (str(obj['data']).split()[0])

        # Three least significant bits identify depth
        self.depth = self.flags & self.openCVMaxDepth

        # Identify cv::Mat depth type and its respective byte size
        self.typeName = self.openCVTypeNames[int(self.depth)]
        self.bytes = self.openCVTypeSizes[self.typeName]

        # Max channels is 511, identified by 9 bits after depth
        self.channels = ((self.flags >> self.openCVDepthBits) &
                         (self.openCVMaxChannels-1)) + 1

class TypeParser():
    """Type Parser"""

    def testCVMat(self, obj):
        mat = PyCVMat(obj)

        # OpenCV's magic value is 0x42ff0000, also packed in flags
        if (mat.flags & mat.openCVMagicValMask != mat.openCVMagicVal):
            return False
        if (mat.depth < 0 or mat.depth > mat.openCVMaxDepth):
            return False
        if (mat.channels < 1 or mat.channels > mat.openCVMaxChannels):
            return False
        if (mat.rows < 1):
            return False
        if (mat.cols < 1):
            return False
        return True

    def cvMat2NumpyArray(self, obj):
        mat = PyCVMat(obj)

        size = mat.rows * mat.step
        dbgInt = DebuggerInterface.DebuggerInterface().factory('gdb')
        mem = dbgInt.readMemory(int(mat.data, 16), size)

        img = np.asarray(bytearray(mem))

        memCols = mat.step / mat.channels
        img = img.reshape(mat.rows, memCols, mat.channels)
        img = img[0:mat.rows, 0:mat.cols, :]

        vis = Visualizer.Visualizer().factory('opencv')
        vis.visualize(img)

    def parse (self, val):
        if (self.testCVMat(val)):
            self.cvMat2NumpyArray(val)
        else:
            raise TypeError("Couldn't identify type or type not supported")
