ctemps = [-40.0, 0.0, 37.0, 75.0, 100.0]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for c in ctemps:
    f = ((9 * c) / 5) + 32
    print(f"{c} C is {f} F")

print()

clean_fruits = [f.strip().lower() for f in fruits]

print(clean_fruits)
