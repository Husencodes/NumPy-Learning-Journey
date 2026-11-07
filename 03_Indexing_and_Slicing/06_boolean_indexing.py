import numpy as np

arr = np.array([10, 25, 30, 45, 50, 65])

print("Values greater than 30:")
print(arr[arr > 30])

print("Even numbers:")
print(arr[arr % 2 == 0])