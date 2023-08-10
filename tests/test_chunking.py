import pickle

import numpy as np
import pytest

from yann_utils.chunking import (chunk_obj, get_chunks, persist_chunks,
                                 reconstruct_obj)


@pytest.fixture
def large_object():
  size_gb = 0.2
  n_elements = int(size_gb * 1e9 // 8 * 1.07)
  array_float64 = np.zeros(n_elements, dtype=np.float64)
  return array_float64


def test_chunking(large_object):
  chunks = chunk_obj(large_object, 10)
  persist_chunks(chunks, "out", "obj")

  chunks = get_chunks("out")
  assert reconstruct_obj(chunks) == pickle.dumps(large_object)
