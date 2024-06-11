
import sys   # Import the sys module 

print("sys.argv:", sys.argv) # Print all parameters, including script itself
print("script name:", sys.argv[0])

first_arg = sys.argv[1]  # Get the first actual parameter
print(f"{first_arg = }")
