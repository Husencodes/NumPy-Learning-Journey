import numpy as np
import time

size = 1_000_000

a = list(range(size))
b = np.arange(size)

# Python execution time
start = time.time()

result = [x * 2 for x in a]

python_time = time.time() - start

# NumPy execution time
start = time.time()

result = b * 2

numpy_time = time.time() - start

print("Python time:", python_time)
print("NumPy time:", numpy_time)