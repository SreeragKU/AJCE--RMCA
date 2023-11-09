import csv
import pandas as pd
fields = ['Name', 'Branch', 'Semester', 'CGPA']
rows = [['Sreerag', 'RMCA', '1', '8.8'],
        ['Stephin', 'RMCA', '1', '7.5'],
        ['Amal', 'RMCA', '1', '8.5'],
        ['Mithun', 'IntMCA', '7', '9.5'],
        ['Rahul', 'MCE', '3', '7.8']]
filename = "SemesterReport.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
df = pd.read_csv("SemesterReport.csv")
print(df.head())