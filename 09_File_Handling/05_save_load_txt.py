import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Save as text
np.savetxt("numbers.txt", arr, fmt="%d")

# Load text
data = np.loadtxt("numbers.txt")

print("Loaded Data:")
print(data)