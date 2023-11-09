import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

sns.kdeplot(data, fill=True, color='blue', label='Density Plot')

plt.xlabel('X-Axis Label')
plt.ylabel('Density')
plt.title('Density Plot Example')

plt.show()
