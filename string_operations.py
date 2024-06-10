band = "foo Fighters"

print(band)
print(type(band))
print(len(band))
print(band.upper())

#  function(obj)
#  obj.method()
print(band.lower(), band.title())
b = band.lower()
print(band)
print(b)

print("fight" in band)
print("Fight" in band)
print("fight" in band.lower())
print()
print(band.count('f'))
print(band.lower().count('f'))
print(band.lower().count('foo'))

print(band.find('Fight'))
print(band.find("mango"))

#  "foo Fighters"
#             1
#   012345678901  

print(band.startswith('foo'))
print(band.startswith('bar'))

print(band.replace('foo', 'food'))
print(band.removesuffix('ers'))
print(band.replace('foo', 'food').removesuffix('ers'))

data = 'taco:mango:penguin:parfait'
words = data.split(':')
print(words)

sentence = "You are not the kumquat haagen-daz"
print(sentence.split())

