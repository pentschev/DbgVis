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

import os
import unittest
import cv2
import numpy as np

class DbgVisTest(unittest.TestCase):

    def test_gdb_cvmat(self):
        os.system("gdb ../build/cv_imread < list_gdb_cmd.txt > /dev/null")
        baseImg = cv2.imread("../samples/bansko.png")
        testImg = cv2.imread("test_out.png")
        self.assertTrue(np.array_equal(testImg, baseImg))
        os.remove("test_out.png")

    def test_gdb_cvmat_roi(self):
        os.system("gdb ../build/cv_imread < list_gdb_cmd_roi.txt > /dev/null")
        baseImg = cv2.imread("../samples/bansko.png")
        baseImgRoi = baseImg[100:200, 100:200]
        testImg = cv2.imread("test_out.png")
        self.assertTrue(np.array_equal(testImg, baseImgRoi))
        os.remove("test_out.png")

if __name__ == "__main__":
    unittest.main()
