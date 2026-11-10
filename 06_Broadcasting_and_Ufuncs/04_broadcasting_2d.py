import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])

result = a + b

print("Original Array:")
print(a)

print("Broadcasting Array:")
print(b)

print("Result:")
print(result)