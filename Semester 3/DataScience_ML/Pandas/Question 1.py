import pandas as pd
df = pd.read_csv("sales_data.csv")
print(df.head())
print("Number of rows: ", len(df))
print("Number of columns: ", len(df.columns))
print("Total Revenue: ", sum(df['Revenue']))
