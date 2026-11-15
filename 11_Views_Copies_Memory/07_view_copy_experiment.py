import numpy as np

original = np.array([10, 20, 30, 40, 50])

view_array = original.view()
copy_array = original.copy()

view_array[0] = 100
copy_array[1] = 200

print("Original:", original)
print("View:", view_array)
print("Copy:", copy_array)

print("View shares memory:",
      np.shares_memory(original, view_array))

print("Copy shares memory:",
      np.shares_memory(original, copy_array))