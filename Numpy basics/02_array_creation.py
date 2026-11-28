# Importing the NumPy library
import numpy as np

# Displaying the program title
print("Creating arrays")

# 1D Array (One-Dimensional Array)
# Creating an array containing 10 elements
arr1 = np.array([1,2,3,4,5,6,7,8,9,0])

# 2D Array (Two-Dimensional Array)
# Creating an array with 3 rows and 3 columns
arr2 = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])

# 3D Array (Three-Dimensional Array)
# Creating a 3D array containing one 3x3 matrix
arr3 = np.array([[[100,200,300],
                  [400,500,600],
                  [700,800,900]]])

# Displaying the 1D array
print("1D array:-", arr1)

# Displaying the 2D array
print("2D array:-", arr2)

# Displaying the 3D array
print("3D array:-", arr3)
