import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# Save
np.save("student_marks.npy", arr)

# Load
data = np.load("student_marks.npy")

print("Original Array:")
print(arr)

print("Loaded Array:")
print(data)