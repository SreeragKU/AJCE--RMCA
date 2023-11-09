import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
sum = arr1 + arr2
pdt = arr1 * arr2
print("Sum: ", sum)
print("Product: ", pdt)

mtx1 = np.array([[1,2],[3,4]])
mtx2 = np.array([[4,5],[7,8]])
multi = np.dot(mtx1, mtx2)
print("Dot Product: \n", multi)