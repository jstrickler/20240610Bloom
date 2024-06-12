fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f0 = sorted(fruits)
print(f"{f0 = }\n")

# str.lower
name = "Bob Smith"
print(str.lower(name), '\n')

f1 = sorted(fruits, key=str.lower)
print(f"{f1 = }\n")

def ignore_case(fruit):
    comparison_value = fruit.lower()
    print(f"Comparing {fruit} as {comparison_value}")
    return comparison_value

f2 = sorted(fruits, key=ignore_case)
print(f"{f2 = }\n")

f3 = sorted(fruits, key=len)
print(f"{f3 = }\n")

def john_sort(s):
    return len(s), s.lower()    # sort by len, then lower-case name

f4 = sorted(fruits, key=john_sort)
print(f"{f4 = }\n")

def wacky(fruit):
    return fruit[-1].lower()

f5 = sorted(fruits, key=wacky)
print(f"{f5 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_product(person):
    return person[2].lower()

for person in sorted(people, key=by_product):
    print(person)
print('-' * 60)

# lambda param:return-value

# sort by DOB
for person in sorted(people, key=lambda p: p[3]):
    print(person)

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{sorted(airports) = }\n")

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)
print(airports.items())
print('-' * 60)

def by_value(item):
    return item[1], item[0]

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)
print('-' * 60)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruits.sort()
print(f"{fruits = }\n")

for fruit in sorted(fruits, reverse=True):
    print(fruit)














