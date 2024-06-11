import os

x = 0

if x:
    print("whoo-hoooo")


if os.path.exists('pastable.py'):
    print("pastable.py exists")
else:
    print("It does not exist")

brocolli = False

font_color = 'red' if brocolli else 'blue'
print(font_color)

#  == != < > >= <=



if (x > 0) and brocolli:
    print("blertz!!")

if (x > 0) or brocolli:
    print("niblurks")








