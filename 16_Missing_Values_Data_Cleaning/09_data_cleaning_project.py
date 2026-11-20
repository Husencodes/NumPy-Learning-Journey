import numpy as np

marks = np.array([
    85, 90, np.nan, 75, 60,
    np.nan, 95, 80, 70, 88
])

print("Original Marks:")
print(marks)

# Count missing values
missing = np.isnan(marks).sum()
print("\nMissing Values:", missing)

# Calculate average without NaN
average = np.nanmean(marks)
print("Average Marks:", average)

# Replace missing values with average
marks[np.isnan(marks)] = average

print("\nCleaned Marks:")
print(marks)

print("\nFinal Average:", np.mean(marks))