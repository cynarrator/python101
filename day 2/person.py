person = {
    "name": "Ram",
    "age": 20,
    "percentage": 9.9,
    "family_members": [
        'mom',
        'dad',
        'sister'
    ],
    'hobby': (
        'reading',
        'watching anime'
    )
}
print(f"Name: {person['name']}")
print(f"Age: {person['age']} years old")
print(f"Percentage: {person['percentage']}%")
print(f"Hobbies include {person['hobby'][0]} and {person['hobby'][1]}")
print(f"Family members include {person['family_members'][0]}, {person['family_members'][1]} and {person['family_members'][2]}")

# To get only to dad from person
print(person['family_members'][1])

# To get the d from dad
print(person['family_members'][1][-1])