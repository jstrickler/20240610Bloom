
numpairs = [(5, 1), (1, 5), (5, 0), (0, 5)]

total = 0

for x, y in numpairs:
    try:  # try some code
        quotient = x / y
    except ZeroDivisionError as err:  # catch error
        print(f"uh-oh, when y = {y}, {err}")
    else:  # no errors!
        total += quotient  # Only if no exceptions were raised
print(total)

