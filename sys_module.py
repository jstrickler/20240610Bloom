import sys

print(f"{sys.prefix = }\n")

print(f"{sys.executable = }\n")

print(f"{sys.version = }\n")

print(f"{sys.version_info = }\n")

print(f"{sys.platform = }\n")

if sys.platform == "win32":
    temp_folder = "C:/temp"
else:
    temp_folder = "/tmp"


print("Life is good....")

sys.stdout.write("Life is good...." + "\n")

print("Life is rotten", file=sys.stderr)



