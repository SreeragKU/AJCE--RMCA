import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the heatmap data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 13, 18, 20]
data_values = [10, 15, 13, 18, 20]
df = pd.DataFrame({'x': x_values, 'y': y_values, 'value': data_values})
heatmap_data = df.pivot_table(index='x', columns='y', values='value')

# Create a scatter plot based on heatmap data
x_scatter = df['x']
y_scatter = df['y']
values = df['value']

plt.scatter(x_scatter, y_scatter, c=values, cmap='YlGnBu', marker='o', label='Data Points')
plt.colorbar(label='Value')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot Based on Heatmap Data')
plt.show()
