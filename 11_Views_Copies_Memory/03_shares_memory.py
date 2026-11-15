import numpy as np

a = np.array([1, 2, 3, 4])

b = a.view()
c = a.copy()

print(np.shares_memory(a, b))
print(np.shares_memory(a, c))