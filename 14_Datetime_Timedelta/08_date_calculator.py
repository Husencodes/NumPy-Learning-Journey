import numpy as np

start_date = np.datetime64('2026-11-18')
end_date = np.datetime64('2026-12-18')

difference = end_date - start_date

print("Date Calculator")
print("--------------------")

print("Start Date:", start_date)
print("End Date:", end_date)

print("Total Days:",
      difference / np.timedelta64(1, 'D'))

print("After 30 Days:",
      start_date + np.timedelta64(30, 'D'))

print("After 2 Months:",
      start_date + np.timedelta64(2, 'M'))