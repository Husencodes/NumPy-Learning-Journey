import numpy as np

marks = np.array([35, 75, 45, 90, 60])

result = np.where(marks >= 50, "Pass", "Fail")

print(result)