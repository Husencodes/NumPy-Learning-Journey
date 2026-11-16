import numpy as np

numbers = [1, 2, 3, 4, 5]

# Python loop
result = []

for num in numbers:
    result.append(num * 2)

print("Loop:", result)

# NumPy
arr = np.array(numbers)

print("NumPy:", arr * 2)