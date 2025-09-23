'''
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
'''

import sys, numpy as np

lst = list(range(1000))
arr = np.arange(1000)

print("List size:", sys.getsizeof(lst))      # size of list container only (not elements)
print("NumPy size:", arr.nbytes)             # actual memory used by all elements

