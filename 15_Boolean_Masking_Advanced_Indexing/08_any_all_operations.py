import numpy as np

arr = np.array([10, 20, 30, 40])

print("Any above 25:", np.any(arr > 25))
print("All above 5:", np.all(arr > 5))