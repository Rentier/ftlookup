import unittest

import numpy as np

import ftlookup

class FtlookupTest(unittest.TestCase):
    def setUp(self):
        self.sut = ftlookup.FastTextWrapper()
        self.sut.loadModel('data/alice.bin')

    def test(self):
        with open('data/vectors.w2vt') as f:
            for line in f:
                word, *entries = line.split()

                expected_embedding = np.array(entries).astype(np.float)
                actual_embedding = self.sut.getVector(word)

                msg = 'Vector for [{0}] did not match! Expected: {1}, was {2}'.format(word, expected_embedding, actual_embedding)
                assert np.allclose(expected_embedding, actual_embedding, atol=0.000001), msg
