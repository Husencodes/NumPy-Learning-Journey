import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Sum:", np.add.reduce(arr))
print("Product:", np.multiply.reduce(arr))
print("Cumulative Sum:", np.add.accumulate(arr))
print("Cumulative Product:", np.multiply.accumulate(arr))