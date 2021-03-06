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

import sys

class DebuggerInterface(object):
    """Debugger Interface"""

    def factory(type):
        if type == "gdb":
            import gdb
            return DebuggerInterfaceGDB()
        assert 0, "Wrong debugger or not yet supported: " + type
    factory = staticmethod(factory)

class DebuggerInterfaceGDB():
    """GDB Debugger Interface"""

    def getSelectedFrame(self):
        import gdb
        return gdb.selected_frame()

    def readVar(self, frame, name):
        import gdb
        return frame.read_var(name)

    def readField(self, var, fieldName):
        import gdb
        return var[fieldName]

    def readMemory(self, address, size):
        # TODO: import gdb at a single, general place
        import gdb
        return gdb.selected_inferior().read_memory(address, size)

    def getPointerAddressFromValue(self, val):
        import gdb
        return val.cast(gdb.lookup_type('size_t'))
