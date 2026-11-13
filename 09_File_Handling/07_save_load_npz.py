import numpy as np

marks = np.array([85, 90, 95])
attendance = np.array([90, 85, 98])

# Save compressed arrays
np.savez_compressed(
    "student_data.npz",
    marks=marks,
    attendance=attendance
)

# Load arrays
data = np.load("student_data.npz")

print("Marks:", data["marks"])
print("Attendance:", data["attendance"])

data.close()