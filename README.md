# DbgVis: The Debugger Visualizer

## Introduction

DbgVis is a library that helps in visualizing data from within a debugger. Most
debuggers are very powerful and allow developers to see every single bit of code
and data associated to it, but, unfortunately, nothing more than the bits.
However, there are times in debugging where visualizing the data could be
extremely useful, let it be a graph or a image.

The purpose of DbgVis is to allow debuggers to display data in a more useful
format to the developer than as a string of bytes.

DbgVis' design aims to be extensible in 3 aspects:

* Data parsing
* Visualization backend
* Debugger backend

### Data parsing

DbgVis allows new data types support to be added.

Currently supported types are:

* OpenCV's Mat

Planned types:

* OpenCV's UMat (OpenCL)
* OpenCV's GpuMat (CUDA)

### Visualization backend

Currently supported visualizers are:

* OpenCV's built-in GUI (imshow)

Planned visualizers:

* Matplotlib
* Pillow

### Debugger backend

Currently supported debuggers are:

* GDB

Planned debuggers:

* LLDB

## Requirements

* GDB with Python 3 support
* Python 3
* OpenCV 3.0+ (compiled with Python support)
* Numpy

## Usage

Clone DbgVis repository:

    git clone https://github.com/pentschev/DbgVis.git

Add DbgVis repository to Python module search path:

    export PYTHONPATH=$(pwd)/DbgVis:${PYTHONPATH}

Now GDB is ready to display images. From the GDB terminal you can now import the
DbgVis interface for GDB:

    source /path/to/DbgVis/gdb.py

There are currently two commands available:

* `show_cv_mat`
* `show_cv_mat_ptr`

The first one can be used to display a `cv::Mat` from a value (e.g., a local
scope variable), whereas the second allows displaying a `cv::Mat` from a pointer
(or a memory address) from the inferior
([inferior](https://sourceware.org/gdb/onlinedocs/gdb/Inferiors-and-Programs.html#Inferiors-and-Programs)
is the GDB terminology for a processing running within GDB or attached to it).

Both `show_cv_mat` and `show_cv_mat_ptr` take exactly one argument: the value
and memory address to a cv::Mat, respectively.

WARNING: API is experimental and subject to change.
