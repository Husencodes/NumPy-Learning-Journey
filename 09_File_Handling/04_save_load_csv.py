import numpy as np

arr = np.array([
    [101, 85],
    [102, 90],
    [103, 95]
])

# Save as CSV
np.savetxt(
    "students.csv",
    arr,
    delimiter=",",
    fmt="%d",
    header="ID,Marks",
    comments=""
)

# Load CSV
data = np.loadtxt(
    "students.csv",
    delimiter=",",
    skiprows=1
)

print("Loaded CSV Data:")
print(data)