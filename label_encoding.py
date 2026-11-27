
# Question:
# Write a Python program to convert categorical
# data into numerical values using Label Encoding.

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {'Color': ['Red', 'Green', 'Blue', 'Red']}

df = pd.DataFrame(data)

encoder = LabelEncoder()

df['Color'] = encoder.fit_transform(df['Color'])

print(df)

# Example:
# Input:  ['Red', 'Green', 'Blue', 'Red']
# Output: [2, 1, 0, 2]
