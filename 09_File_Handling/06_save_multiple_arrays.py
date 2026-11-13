import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

# Save multiple arrays
np.savez("my_data.npz", array1=a, array2=b)

# Load multiple arrays
data = np.load("my_data.npz")

print("Array 1:", data["array1"])
print("Array 2:", data["array2"])