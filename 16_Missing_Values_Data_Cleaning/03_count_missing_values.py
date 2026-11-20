import numpy as np

data = np.array([10, np.nan, 30, np.nan, 50])

count = np.isnan(data).sum()

print("Missing Values:", count)