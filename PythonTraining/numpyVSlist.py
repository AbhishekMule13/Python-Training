import numpy as np
import time

# Python list
lst = list(range(1_000_000))
start = time.time()
[x*2 for x in lst]
print("List time:", time.time() - start)

# NumPy array
arr = np.arange(1_000_000)
start = time.time()
arr*2
print("NumPy time:", time.time() - start)
