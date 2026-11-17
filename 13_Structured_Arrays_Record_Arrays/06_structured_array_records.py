import numpy as np

students = np.array([
    ("Rahul", 20, 85),
    ("Amit", 21, 90)
], dtype=[
    ("name", "U20"),
    ("age", "i4"),
    ("marks", "i4")
])

records = students.view(np.recarray)

print(records.name)
print(records.age)
print(records.marks)