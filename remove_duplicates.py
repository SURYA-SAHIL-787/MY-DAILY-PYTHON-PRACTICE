
# Question:
# Write a Python program to identify and remove
# duplicate records from a dataset.

import pandas as pd

data = {'Marks': [80, 90, 80, 70, 90]}

df = pd.DataFrame(data)

df = df.drop_duplicates()

print(df)

# Example:
# Input:  [80, 90, 80, 70, 90]
# Output: [80, 90, 70]
