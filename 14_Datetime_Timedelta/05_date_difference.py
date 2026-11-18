import numpy as np

start = np.datetime64('2026-11-01')
end = np.datetime64('2026-11-18')

difference = end - start

print("Difference:", difference)
print("Number of Days:", difference / np.timedelta64(1, 'D'))