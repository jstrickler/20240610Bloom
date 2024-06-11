
colors = "red blue green yellow brown black".split()
print(f"{colors = }")


months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
print(f"{months = }\n")

colors_enum = enumerate(colors)
print(f"{colors_enum = }")

for i, color in colors_enum:  # enumerate() returns iterable of (index, value) tuples
    print(i, color)

print()
print(f"{list(colors_enum) = }\n")

print(f"{list(enumerate(colors)) = }\n")


for num, month in enumerate(months, 1):  # Second parameter to enumerate is added to index
    print(f"{num} {month}")
print()

reversed_colors = reversed(colors)
print(f"{reversed_colors = }")

for color in reversed_colors:
    print(color)

