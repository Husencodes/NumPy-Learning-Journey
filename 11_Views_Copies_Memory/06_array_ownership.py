import numpy as np

a = np.array([1, 2, 3, 4])

b = a.view()
c = a.copy()

print("Original owns data:", a.flags.owndata)
print("View owns data:", b.flags.owndata)
print("Copy owns data:", c.flags.owndata)