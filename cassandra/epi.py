import pandas as pd
from cassandra.cluster import Cluster
import csv

# Read CSV into DataFrame
df = pd.read_csv('epi.csv')

# Display the first few rows
# print(df.head())

df_cleaned = df.dropna()
df_cleaned['calories'] = df_cleaned['calories'].astype(int)
df_cleaned['protein'] = df_cleaned['protein'].astype(int)
df_cleaned['fat'] = df_cleaned['fat'].astype(int)
df_cleaned['sodium'] = df_cleaned['sodium'].astype(int)
print(df_cleaned.head())

# print(df_cleaned.columns)
# rows, cols = df_cleaned.shape
# print(rows , cols )




with open('output.txt', 'w') as f:
    for index, row in df_cleaned.iterrows():
        f.write(f"INSERT INTO food_macros (id, title, rating, calories, protein, fat, sodium) VALUES (uuid(), \'{row['title']}\', {row['rating']},{row['calories']}, {row['protein']}, {row['fat']},{row['sodium']});\n")
    


# Sample DataFrame
# data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
# df = pd.DataFrame(data)

# Open a file to write
# with open('output.txt', 'w') as f:
#     for index, row in df.iterrows():
#         f.write(f"Row number: {index}, Name: {row['name']}, Age: {row['age']}\n")

# print("File 'output.txt' has been created successfully.")
