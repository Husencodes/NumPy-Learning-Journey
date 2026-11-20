import numpy as np

data = np.array([10, 20, np.nan, 40, 50])

print("Mean:", np.nanmean(data))
print("Median:", np.nanmedian(data))
print("Sum:", np.nansum(data))