import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([7, 8, 9, 10, 11, 12])
arr3 = np.array([[4, 5, 6], [1, 2, 3]])

print("Shape of array: ",arr2.shape)
print("Number of dimensions: ",arr2.ndim)
print("Data Type: ",arr1.dtype)
print("Reshape: \n", arr1.reshape(2,3))
print("Concatenate: ", np.concatenate((arr1,arr2), axis = 0))
print("Split: ", np.array_split(arr1, 3))
