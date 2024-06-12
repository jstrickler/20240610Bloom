state_capitals = {}  # new, empty, dictionary
state_capitals = dict()  #  same

state_capitals['NC'] = 'Raleigh'
state_capitals['MN'] = 'St. Paul'
state_capitals['VA'] = 'Richmond'

print(f"{state_capitals = }\n")

print(f"{state_capitals['MN'] = }")
# print(f"{state_capitals['CA'] = }")

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



print(airports['MCO'])

airports['SLC'] = 'Salt Lake City'
airports['MCO'] = 'Disney World'
print(f"{airports['MCO'] = }")

print(airports['SLC'])  # print value where key is 'SLC'

code = 'PSP'

if code in airports:   # is key in dictionary?
    print(airports[code])  # print key if key is in dictionary
else:
    print(f"{code} not in airports")

print(airports.get(code))  # get value if key in dict, otherwise get None
print(airports.get(code, 'NO SUCH AIRPORT'))  # get value if key in dict, otherwise get 'NO SUCH AIRPORT'

print(airports.setdefault(code, 'Palm Springs'))  # get value if key in dict, otherwise get 'Palm Springs' AND set key
print(code in airports)  # check for key in dict

print(f"{airports = }\n")

print(f"{airports.items() = }\n")

for code, city in airports.items():
    print(code, city)
print()