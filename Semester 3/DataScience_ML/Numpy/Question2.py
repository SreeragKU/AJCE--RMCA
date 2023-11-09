import numpy as np
grades = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
print("Average grade: ", np.mean(grades))
ftgrade = grades[grades > 90]
print("Number of Students scoring above 90: ", len(ftgrade))
stdgd = np.std(grades)
print("Standard deviation of grades: ", np.round(stdgd, decimals=2))