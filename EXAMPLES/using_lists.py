things = []  # empty list
names = list()  # empty list

cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)    # LIST.extend(iterable)
print(f"cities: {cities}\n")

#  LIST.append(object)  LIST.insert(pos, object) LIST.extend(iterable)

del cities[3]
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()   # removes last element
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

#  del LIST[pos]  LIST.remove(value)   LIST.pop(pos)

print(f"{cities[0] = }")
print(f"{cities[3] = }")

print(f"{cities[-1] = }")
print(f"{cities[-2] = }")

