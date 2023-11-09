import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[4, 5,6], [1, 2, 3]])
arrZ = np.zeros(5)
arrO = np.ones((2, 3))
arrId = np.eye(3)
arrR = np.arange(0, 10, 2)
print("One dimensional array: ",arr1)
print("Two dimensional array: \n",arr2)
print("Array of zeroes",arrZ)
print("Array of ones: \n",arrO)
print("Identity array: \n",arrId)
print("Range of values: ",arrR)
arr3 = []
print("Before Append: ", arr3)
arr3.append(arr1)
print("Append Array: ", arr3)
