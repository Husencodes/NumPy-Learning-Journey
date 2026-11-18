import numpy as np

date = np.datetime64('2026-11-18')

new_date = date + np.timedelta64(10, 'D')

print("Original Date:", date)
print("After 10 Days:", new_date)