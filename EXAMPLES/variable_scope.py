x = 5  # GLOBAL variable

def spam():
    x = 22  # Local variable; does not modify global x
    print("spam(): x is", x)
    y = "wolverine"  # Local variable
    print("spam(): y is", y)


def eggs():
    print("eggs(): X is", x)  # Uses global x since there is no local x
    y = "wolverine"
    print("eggs(): y is", y)


spam()
print()
eggs()
print()
print("main: x is ", x)
