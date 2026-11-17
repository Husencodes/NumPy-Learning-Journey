import numpy as np

students = np.array([
    ("Rahul", 20, 85.5),
    ("Amit", 21, 90.0),
    ("John", 19, 78.5)
], dtype=[
    ("name", "U20"),
    ("age", "i4"),
    ("marks", "f4")
])

print(students)