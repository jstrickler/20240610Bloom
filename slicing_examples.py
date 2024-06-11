fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits = }\n")
print(f"{len(fruits) = }\n")

print(f"{fruits[0:4] = }\n")

# slice
#  LIST[start-at:stop-before:count-by]
print(f"{fruits[:4] = }\n")
print(f"{fruits[15:] = }\n")

print(f"{fruits[3:9] = }\n")

print(f"{fruits[2:7] = }\n")

band = "Foo Fighters"
print(f"{band[4:9] = }\n")
print(f"{band[:3] = }\n")

print(f"{band[::2] = }\n")

print(f"{band[::] = }")
print(f"{band[0:len(band):1] = }")

print(f"{fruits = }\n")

print(f"{fruits[-5:] = }\n")
print(f"{fruits[::3] = }\n")
print(f"{fruits[2:12:2] = }\n")

#  for VAR ... in ITERABLE:
#     ...
for wombat in fruits:
    # fruit = fruits[0]
    # fruit = fruits[1]
    # ...
    print(wombat, len(wombat), wombat.upper(), wombat[:3].title())
print()

colors = ['red', 'purple', 'green']

# for var in sequency-thing:  # AKA 'iterable'
for tint in colors:
    print(f"Paint it {tint}")
print()

print(f"{band = }\n")
for c in band:
    print(c)
print()
