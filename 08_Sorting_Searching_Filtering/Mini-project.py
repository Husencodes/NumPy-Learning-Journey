import numpy as np

marks = np.array([85, 45, 92, 67, 92, 35, 78])

# Sort marks
sorted_marks = np.sort(marks)[::-1]

# Find students who passed
passed = marks[marks >= 40]

# Find highest marks
highest = np.max(marks)

# Find unique marks
unique_marks = np.unique(marks)

print("Original Marks:", marks)
print("Ranked Marks:", sorted_marks)
print("Passed Marks:", passed)
print("Highest Marks:", highest)
print("Unique Marks:", unique_marks)