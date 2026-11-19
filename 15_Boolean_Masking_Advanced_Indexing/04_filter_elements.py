import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30])

even = arr[arr % 2 == 0]

print("Even Numbers:", even)