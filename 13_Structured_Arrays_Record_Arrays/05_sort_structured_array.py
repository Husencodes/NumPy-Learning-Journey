import numpy as np

students = np.array([
    ("Rahul", 20, 85),
    ("Amit", 21, 90),
    ("John", 19, 78)
], dtype=[
    ("name", "U20"),
    ("age", "i4"),
    ("marks", "i4")
])

sorted_students = np.sort(students, order="marks")

print(sorted_students)