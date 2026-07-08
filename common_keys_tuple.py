# Program to find common keys from two dictionaries
# and store their values as tuples

dict1 = {
    "Python": 90,
    "Java": 80,
    "C": 70,
    "HTML": 85
}

dict2 = {
    "Python": 95,
    "C": 75,
    "CSS": 88,
    "HTML": 92
}

common_data = {}

for key in dict1:
    if key in dict2:
        common_data[key] = (dict1[key], dict2[key])

print("First Dictionary:")
print(dict1)

print("\nSecond Dictionary:")
print(dict2)

print("\nCommon Keys with Tuple Values:")
print(common_data)
