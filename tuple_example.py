location = 45.3903, 38.39039
location = (45.3903, 38.39039)
print(f"{location = }\n")
print(f"{location[0] = }")
print(f"{location[1] = }")

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'
print(f"{person[0] = }")
print(f"{person[1] = }")

first_name, last_name, product, dob = person   # iterable unpacking
print(f"{len(person) = }")


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

print(f"{people[0] = }\n")
print(f"{type(people[0]) = }\n")
print(f"{people[0][2] = }")
print(f"{people[0][2][1] = }")
print()

for person in people:
    print(person[-1])
print()

# for VAR, VAR, ... in ITERABLE:
#    ...
for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = people[0]
    # first_name, last_name, product, dob = people[1]
    # ...
    print(last_name, dob)
print()


my_data = [('pink', 4), ('navy', 6), ('purple', 2)]

for color, number in my_data:
    print(f"{color}: {number}")
print()









