import numpy as np

data = np.array([10, np.nan, np.inf, -np.inf])

cleaned = np.nan_to_num(
    data,
    nan=0,
    posinf=100,
    neginf=-100
)

print("Original:", data)
print("Cleaned:", cleaned)