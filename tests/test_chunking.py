import pickle

import numpy as np
import pytest

from yann_utils.chunking import chunk_obj, get_chunks, persist_chunks, reconstruct_obj


@pytest.fixture
def large_object():
  """Return a large object."""
  size_gb = 1
  n_elements = int(size_gb * 1e9 // 8 * 1.07)
  array_float64 = np.zeros(n_elements, dtype=np.float64)
  return array_float64


def test_reconstruction_in_nested_dir(large_object):
  """Test reconstruction of an object from chunks in a nested directory."""
  chunks = chunk_obj(large_object, 10)
  dir = "out/a"
  persist_chunks(chunks, dir)

  chunks = get_chunks(dir)
  assert reconstruct_obj(chunks) == pickle.dumps(large_object)


def test_reconstruction_given_chunk_size_larger_than_object(large_object):
  """Test reconstruction of an object where the chunk size is larger than the object."""
  chunks = chunk_obj(large_object, 10000)
  dir = "out/b"
  persist_chunks(chunks, dir)

  chunks = get_chunks(dir)
  assert reconstruct_obj(chunks) == pickle.dumps(large_object)
