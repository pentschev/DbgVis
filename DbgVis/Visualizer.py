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

import numpy as np
import cv2

class Visualizer(object):
    """Visualizer Factory"""

    def factory(type):
        if type == "opencv": return VisualizerCV()
        if type == "tester": return VisualizerTester()
        assert 0, "Wrong or not supported visualizer type '" + type + "'"
    factory = staticmethod(factory)

class VisualizerCV():
    """OpenCV Visualizer"""

    def passFunc(i, v):
        pass

    def visualize(self, obj):
        cv2.namedWindow('image')

        normalizeSwitch = 'Normalize Output:\n0 = OFF, 1 = ON'
        cv2.createTrackbar(normalizeSwitch, 'image', 0, 1, self.passFunc)

        while(True):
            normalize = cv2.getTrackbarPos(normalizeSwitch, 'image')

            if (normalize):
                diff = obj.max() - obj.min()
                adjustedObj = np.uint8(((obj - obj.min()) / diff) * 255)
            else:
                adjustedObj = obj

            cv2.imshow('image', adjustedObj)
            k = cv2.waitKey(1)

            if chr(k) == 's':
                self.save(adjustedObj)

            # ESC key closes window
            if k == 27:
                break

        cv2.destroyAllWindows()

class VisualizerTester():
    """Tester Visualizer"""

    def visualize(self, obj):
        cv2.imwrite('test_out.png', obj)
