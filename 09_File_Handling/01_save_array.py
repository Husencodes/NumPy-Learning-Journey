import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Save array into a file
np.save("my_array.npy", arr)

print("Array saved successfully!")