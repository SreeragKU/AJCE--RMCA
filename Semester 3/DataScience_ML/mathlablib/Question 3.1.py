import matplotlib.pyplot as plt
import pandas as pd

x_values = [1, 2, 3, 4, 5]
data_values = [10, 15, 13, 18, 20]

df = pd.DataFrame({'x': x_values, 'value': data_values})

plt.scatter(df['x'], df['value'], marker='o', color='blue', label='Data Points')
plt.xlabel('No. of students')
plt.ylabel('Values')
plt.title('Scatter Plot based on Heatmap Values')
plt.show()
