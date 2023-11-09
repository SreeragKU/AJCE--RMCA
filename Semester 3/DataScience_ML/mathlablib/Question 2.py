import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

marks = np.array([18,34,37,
              45, 49, 27,
              31, 35, 42])

plt.figure(figsize=(4, 4))
sns.boxplot(y=marks, color='darkcyan')
plt.title('Quartile Plot: Exam Score')
plt.ylabel('Score')
plt.show()

