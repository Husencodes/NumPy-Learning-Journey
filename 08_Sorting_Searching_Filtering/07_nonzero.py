import numpy as np

arr = np.array([0, 10, 0, 20, 30, 0])

result = np.nonzero(arr)

print("Original:", arr)
print("Non-zero positions:", result)
print("Non-zero values:", arr[result])