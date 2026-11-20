import numpy as np

data = np.array([10, 20, np.nan, 40, np.nan])

result = np.isnan(data)

print("Missing Values:", result)