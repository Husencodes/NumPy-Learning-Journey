import numpy as np

marks = np.array([45, 78, 90, 35, 88])

mask = marks >= 50

print("Mask:", mask)
print("Passed Marks:", marks[mask])