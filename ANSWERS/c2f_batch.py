import sys

celsius = float(sys.argv[1]) #  

fahrenheit = ((9 * celsius) / 5) + 32

# print(f"{celsius:.1f} C is {fahrenheit:.1f} F")
print(celsius, fahrenheit)

#        argv[0]       argv[1]
# python c2f_batch.py   100