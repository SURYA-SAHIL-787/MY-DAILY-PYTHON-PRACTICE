
# Question:
# Write a Python program to handle missing values
# in a dataset using mean imputation.

import pandas as pd

data = {'Marks': [80, 90, None, 70, 60]}

df = pd.DataFrame(data)

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print(df)

# Example:
# Input:  [80, 90, None, 70, 60]
# Output: [80, 90, 75, 70, 60]
