import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, 3)

print("Original Array:", arr)

print("Split Arrays:")
for item in result:
    print(item)