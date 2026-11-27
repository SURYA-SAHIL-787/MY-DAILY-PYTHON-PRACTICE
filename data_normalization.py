
# Question:
# Write a Python program to normalize numerical
# data between 0 and 1 using Min-Max Scaling.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {'Marks': [20, 40, 60, 80, 100]}

df = pd.DataFrame(data)

scaler = MinMaxScaler()

df['Marks'] = scaler.fit_transform(df[['Marks']])

print(df)

# Example:
# Input:  [20, 40, 60, 80, 100]
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
