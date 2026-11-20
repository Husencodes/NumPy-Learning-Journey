import numpy as np

data = np.array([10, 20, np.inf, 40, -np.inf])

print("Infinite Values:", np.isinf(data))

print("Finite Values:", np.isfinite(data))