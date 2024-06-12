def main():
    while True:
        expr = input("Enter a math expression: ")

        if expr.lower() == 'q':
            break

        v1, op, v2 = expr.split()
        # should trap errors here
        try:
            v1 = float(v1)
            v2 = float(v2)
        except ValueError as err:
            print(err)
            print("Please enter NUMBER OPERATOR NUMBER")
            continue   # go back to top of loop


        if op == '+':
            result = add(v1, v2)
        elif op == '-':
            result = sub(v1, v2)
        elif op == '*':
            result = mul(v1, v2)
        elif op == '/':
            result = div(v1, v2)
        else:
            print("Bad operator!")
            continue

        print(f"{result:.3f}")


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x/y

main() # get the party started

