import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("First three:", arr[0:3])
print("Middle elements:", arr[2:5])
print("From index 2:", arr[2:])
print("Before index 4:", arr[:4])
print("Every second:", arr[::2])