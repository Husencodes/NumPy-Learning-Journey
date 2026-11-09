import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original Array:")
print(arr)

print("Sum:", np.sum(arr))
print("Column Sum:", np.sum(arr, axis=0))
print("Row Sum:", np.sum(arr, axis=1))

print("Column Mean:", np.mean(arr, axis=0))
print("Row Mean:", np.mean(arr, axis=1))