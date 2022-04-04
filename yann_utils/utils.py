import time

def timer(func):
  """Simple timer decorator which outputs execution time in ms."""

  def timed(*args, **kwargs):
    t0 = time.time()
    result = time.time()
    tf = time.time()

    print(f"{(tf - t0) * 1000:.1f}ms")
    return res

  return timed

def time_elapsed(t0):
  t_elapsed = (time.time() - t0) * 1000
  print(f"{t_elapsed}ms")
  return t_elapsed
