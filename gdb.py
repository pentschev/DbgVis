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
from DbgVis import TypeParser
from DbgVis import Visualizer

class show_cv_mat (gdb.Command):
    """Display a cv::Mat on the screen"""

    def __init__ (self):
        super (show_cv_mat, self).__init__ ("show_cv_mat", gdb.COMMAND_USER)

    def invoke (self, args, from_tty):
        argv = gdb.string_to_argv(args)

        frame = gdb.selected_frame()
        frameImg = frame.read_var(argv[0])

        tp = TypeParser.TypeParser()
        img = tp.parse(frameImg)

        vis = Visualizer.Visualizer().factory('opencv')
        vis.visualize(img)

class show_cv_mat_ptr (gdb.Command):
    """Display a cv::Mat on the screen"""

    def __init__ (self):
        super (show_cv_mat_ptr, self).__init__ ("show_cv_mat_ptr", gdb.COMMAND_USER)

    def invoke (self, args, from_tty):
        argv = gdb.string_to_argv(args)

        ptr = gdb.parse_and_eval(argv[0])
        ptrAddress = gdb.Value(ptr)
        ptrTyped = ptrAddress.cast(gdb.lookup_type('cv::Mat').pointer())

        tp = TypeParser.TypeParser()
        img = tp.parse(ptrTyped.dereference())

        vis = Visualizer.Visualizer().factory('opencv')
        vis.visualize(img)

show_cv_mat()
show_cv_mat_ptr()
