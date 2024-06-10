import sys
import logging

logging.basicConfig(filename="c2f.log", level=logging.INFO)

try:
    celsius = float(sys.argv[1])
except IndexError as err:
    print("Please provide Celsius value on command line")
    logging.error(err)
except ValueError as err:
    print(f"Cannot convert {sys.argv[1]} to float")
    logging.warning(err)
else:
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f"{celsius:.1f} C is {fahrenheit:.1f} F")
    logging.info(f"fahrenheit value is {fahrenheit}")
