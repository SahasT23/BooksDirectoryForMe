from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import setuptools
import os
import subprocess

class get_pybind_include(object):
    """Helper class to determine the pybind11 include path"""

    def __str__(self):
        import pybind11
        return pybind11.get_include()

ext_modules = [
    Extension(
        'mycompressor',
        sources=[
            'bindings/bindings.cpp',
            'compression/src/compressor.cpp',
        ],
        include_dirs=[
            'compression/include',
            get_pybind_include(),
        ],
        language='c++',
        extra_compile_args=['-std=c++17'],
    ),
]

setup(
    name='mycompressor',
    version='0.1.0',
    author='Your Name',
    description='A C++-backed file compressor with Python bindings',
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
    zip_safe=False,
    install_requires=['pybind11'],
    python_requires='>=3.6',
)
