import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("Random with Uniform Distribution: ",np.random.rand())
print("Random with Standard Normal: ", np.random.randn())
print("Before shuffle: ", arr)
np.random.shuffle(arr)
print("Shuffle: ", arr)
