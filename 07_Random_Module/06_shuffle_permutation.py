import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Shuffle modifies original array
np.random.shuffle(arr)

print("Shuffled Array:", arr)

# Permutation returns a shuffled copy
a = np.array([10, 20, 30, 40, 50])

result = np.random.permutation(a)

print("Original:", a)
print("Permutation:", result)