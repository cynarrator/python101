fruits = (
    'apple',
    'apple',
    'banana',
    'kiwi',
    ['arko_list'],
    1,
    2,
    1.1
)

# Change the first element of the tuple
fruits = list(fruits)
fruits[0] = 'pear'
fruits = tuple(fruits)
print(fruits)