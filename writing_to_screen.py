band = "Foo Fighters"
genre = "rock"
value = 29.326930293432532

print(band)
print(band, genre, value)
print(band, genre, value, sep=',')
print(band, genre, value, sep=', ')
print(band, genre, value, sep='//')
print(band, genre, value, sep=' --- ')
print(band, genre, value, sep='')
print(band, genre, value, sep='\b')  #weird and silly
print()

print(band, end=" ")
# if ...
print(genre)
# else ..
print(value)

#  "rock: Foo Fighters"

# print(genre, ":", band)

# f"{var} {var} {expr} ...""
print(f"{genre}: {band}")
print(f"{band}'s genre is {genre}")
print(f"2 + 2 is {2 + 2}")

#  f"xxx" started in Python 3.6
print(f"value is {value}")
print(f"value is {value:.2f}")


