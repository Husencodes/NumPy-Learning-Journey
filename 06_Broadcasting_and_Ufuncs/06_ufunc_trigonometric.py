import numpy as np

angles = np.array([0, 30, 45, 60, 90])

radians = np.deg2rad(angles)

print("Sine:", np.sin(radians))
print("Cosine:", np.cos(radians))
print("Tangent:", np.tan(radians))