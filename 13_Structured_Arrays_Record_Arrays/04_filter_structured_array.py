import numpy as np

students = np.array([
    ("Rahul", 20, 85),
    ("Amit", 21, 90),
    ("John", 19, 65)
], dtype=[
    ("name", "U20"),
    ("age", "i4"),
    ("marks", "i4")
])

top_students = students[students["marks"] >= 80]

print(top_students)