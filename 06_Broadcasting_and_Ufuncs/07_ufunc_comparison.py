import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([15, 20, 25, 45])

print("Greater:", np.greater(a, b))
print("Less:", np.less(a, b))
print("Equal:", np.equal(a, b))
print("Maximum:", np.maximum(a, b))
print("Minimum:", np.minimum(a, b))