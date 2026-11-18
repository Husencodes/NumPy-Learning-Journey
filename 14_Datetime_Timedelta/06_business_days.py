import numpy as np

start = np.datetime64('2026-11-16')
end = np.datetime64('2026-11-23')

days = np.busday_count(start, end)

print("Business Days:", days)