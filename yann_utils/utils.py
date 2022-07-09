import time
from typing import TypeVar, List
import itertools
import functools
import matplotlib as mpl

T = TypeVar("T")


def timer(func):
  """Simple timer decorator which outputs execution time in ms."""

  def timed(*args, **kwargs):
    t0 = time.time()
    res = func(*args, **kwargs)
    tf = time.time()

    print(f"{(tf - t0) * 1000:.1f}ms")
    return res

  return timed


def time_elapsed(t0):
  t_elapsed = (time.time() - t0) * 1000
  print(f"{t_elapsed}ms")
  return t_elapsed


def flatten(list_o_list: List[List[T]]) -> List[T]:
  return list(itertools.chain(*list_o_list))


def compose(*functions):
  def operation(f, g):
    return lambda x: f(g(x))

  return functools.reduce(operation, functions, lambda x: x)

def clusters_to_cmap(clusters):
  color_wheel = mpl.colormaps["gist_ncar"]
  N = len(set(clusters))
  return [color_wheel(cls / N) for cls in clusters]


class Cache:
  """Persistent and automated caching of objects."""
  locs: List[str] = []

  def __init__(self) -> None:
    if os.path.exists("cache/_cache.pkl"):
      with open("cache/_cache.pkl", "rb") as f:
        mem = pickle.load(f)
        self.locs = mem.locs


  def save(self, obj: Any, name: str) -> None:
    self.locs.append(name)
    with open(f"cache/{name}.pkl", "wb") as f:
      pickle.dump(obj, f)

    with open(f"cache/_cache.pkl", "wb") as f:
      pickle.dump(self, f)

  def load(self, name: str) -> Any:
    with open(f"cache/{name}.pkl", "rb") as f:
      return pickle.load(f)

  def __repr__(self):
    return "\n".join(self.locs)
