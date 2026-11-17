import numpy as np

students = np.array([
    ("Rahul", 20, 85),
    ("Amit", 21, 92),
    ("John", 19, 75),
    ("Sara", 20, 88)
], dtype=[
    ("name", "U20"),
    ("age", "i4"),
    ("marks", "i4")
])

print("All Students:")
print(students)

print("\nTopper:")
topper = students[np.argmax(students["marks"])]
print(topper)

print("\nStudents scoring above 80:")
print(students[students["marks"] > 80])

print("\nAverage Marks:")
print(np.mean(students["marks"]))