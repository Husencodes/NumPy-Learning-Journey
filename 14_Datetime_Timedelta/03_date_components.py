import numpy as np

date = np.datetime64('2026-11-18')

year = date.astype('datetime64[Y]')
month = date.astype('datetime64[M]')

print("Year:", year)
print("Month:", month)
print("Day:", date)