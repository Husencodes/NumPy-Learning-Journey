import numpy as np

data = np.array([10, 20, np.nan, 40, 50])

mean = np.nanmean(data)

data[np.isnan(data)] = mean

print("Cleaned Data:", data)