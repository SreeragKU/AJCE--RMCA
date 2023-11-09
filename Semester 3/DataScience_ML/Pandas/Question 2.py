import pandas as pd
df = pd.read_csv("student_data.csv")
print(df.head())
age = df[df['Age'] > 19]
print("Students who are 20 years old or older: \n", age)

print("Average GPA of all students:",df['GPA'].mean().round(2))

data1 = df.sort_values(by='GPA', ascending= False)
print("Top 5 students with hightest GPA: \n", data1.head(5))

data2 = df.groupby('Age')['GPA'].mean().reset_index()
print("Average GPA by age group: \n", data2)
