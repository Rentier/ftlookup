from cython.operator cimport dereference as deref

from libc.stdint cimport int64_t
from libcpp.string cimport string

cimport numpy as np
import numpy as np

cdef extern from "vector.h" namespace "fasttext":

    cdef cppclass Vector:
        Vector(int64_t) except +
        float * data_

cdef extern from "fasttext.h" namespace "fasttext":

    cdef cppclass FastText:
        FastText() except +
        void loadModel(string)
        void getVector(Vector&, string)
        int getDimension()
      

cdef class FastTextWrapper:
    cdef FastText *c_fasttext      # hold a C++ instance which we're wrapping

    def __cinit__(self):
        self.c_fasttext = new FastText()

    def __dealloc__(self):
        del self.c_fasttext

    def loadModel(self, path_to_model):
        self.c_fasttext.loadModel(path_to_model.encode('utf-8'))

    def getVector(self, word):
        cdef int64_t dim = self.vector_size
        cdef Vector *vec = new Vector(dim)
        self.c_fasttext.getVector(deref(vec), word.encode('utf-8'))
        cdef float[:] view = <float[:dim]> vec.data_
        result = np.array(view, copy=True)
        del vec
        return result

    @property
    def vector_size(self):
        return self.c_fasttext.getDimension()
