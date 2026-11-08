import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vertical Stack:")
print(np.vstack((a, b)))

print("Horizontal Stack:")
print(np.hstack((a, b)))

print("Stack along new axis:")
print(np.stack((a, b)))