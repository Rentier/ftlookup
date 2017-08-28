from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension

import numpy as np

sourcefiles  = [
    'ftlookup/ftlookup.pyx', 
    'fastText/src/args.cc',
    'fastText/src/dictionary.cc',
    'fastText/src/fasttext.cc',
    'fastText/src/matrix.cc',
    'fastText/src/model.cc',
    'fastText/src/productquantizer.cc',
    'fastText/src/qmatrix.cc',
    'fastText/src/utils.cc',
    'fastText/src/vector.cc'
]

compile_opts = ['-std=c++11', '-pthread']
ext=[Extension('*',
            sourcefiles,
            extra_compile_args=compile_opts,
            include_dirs=['fastText/src', np.get_include()],
            language='c++')]

setup(
    name='ftlookup',
    version='0.0.1',
    description='Simple wrapper around Facebook fastText Edit',
    url='https://github.com/Rentier/ftlookup',
    author='Jan-Christoph Klie',
    author_email='git@mrklie.com',
    license='GPL3',
    install_requires=['Cython'],
    test_suite="tests",
    ext_modules=cythonize(ext)
)