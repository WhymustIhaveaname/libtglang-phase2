#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
use `python setup.py build_ext --inplace` to compile tglang.pyx to .so
The --inplace option indicates that the .so should be placed in the current directory instead of the default build directory.
use `cython tglang.pyx --embed --3str` to generate a .c file
"""

from distutils.core import setup
from Cython.Build import cythonize
import numpy
import os


setup(
    ext_modules = cythonize("tglang.pyx"),
    #scripts = ["tglang.pyx"],
    include_dirs=[numpy.get_include()]
)

#os.system('gcc -o tglang.exe tglang.c -lm')
