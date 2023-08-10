#%%
import pytest
from python_utils.chunking import chunk_obj, persist_chunks, get_chunks, reconstruct_obj
import numpy as np
import pickle

size_gb = 0.2
n_elements = int(size_gb * 1e9 // 8 * 1.07)
array_float64 = np.zeros(n_elements, dtype=np.float64)
array_float64.nbytes / 1024**3

chunks = chunk_obj(array_float64, 10)
persist_chunks(chunks, "out", "obj")

chunks = get_chunks("out")
obj = reconstruct_obj(chunks)
assert reconstruct_obj(chunks) == pickle.dumps(array_float64)


#%%
import os
os.getcwd()