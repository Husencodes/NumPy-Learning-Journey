import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Convert 1D into 2D
new_arr = arr.reshape(2, 3)

print("Original Array:")
print(arr)

print("Reshaped Array:")
print(new_arr)

print("New Shape:", new_arr.shape)