import numpy as np

data = np.array([10, np.nan, 30, 40, np.nan, 60])

cleaned = data[~np.isnan(data)]

print("Original:", data)
print("Cleaned:", cleaned)