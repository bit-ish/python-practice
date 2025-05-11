my_dict = {
    "name": "Alice",
    "age": 28,
    "occupation": "Engineer",
    "city": "San Francisco",
    "hobbies": ["Reading", "Hiking", "Painting"],
    "education": {
        "undergraduate": "B.Sc. in Computer Science",

        "graduate": "M.Sc. in Artificial Intelligence"
    },
    "friends": [
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 27},
        {"name": "David", "age": 28}
    ]
}

''' to print out each key from a dictionary. '''

# for key in my_dict:
#     print(key)

''' to print out each values from a dictionary. '''

# for values in my_dict.values():
#     print(values)

''' to print out each key:values pair from a dictionary. '''
# for k,v in my_dict.items():
#     print(f"{k}: {v}")

''' to loop through a list inside a dictionary containing dictionary. '''
for friend in my_dict["friends"]:
    print(f" {friend['name']} is {friend['age']} years old")