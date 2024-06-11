fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f1 = [f.upper() for f in fruits]  # list comprehension
print(f"{f1 = }\n")

fruits_gen = (f.upper() for f in fruits)  # generator expression (iterator, not list)
print(f"{fruits_gen = }\n")
for fruit in fruits_gen:
    print(fruit)
