import numpy as np

dates = np.array([
    '2026-11-15',
    '2026-11-16',
    '2026-11-17',
    '2026-11-18'
], dtype='datetime64[D]')

print("All Dates:", dates)

print("Next 5 Days:", dates + np.timedelta64(5, 'D'))

print("Sorted Dates:", np.sort(dates))