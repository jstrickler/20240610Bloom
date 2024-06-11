max_value = 1_000_001
min_value = 0
tries = 1

while True:
    guess = (max_value + min_value) // 2
    answer = input(f"Is {guess} your number? (h for too high, l for too low, q to quit, y for number) ")

    if answer == "q":
        break

    if answer == "h":
        max_value = guess
    elif answer == "l":
        min_value = guess
    elif answer == "y":
        print(f"I got it in {tries} tries!")
        break
    else:
        print("Please enter h, l, or y")

    if answer == "h" or answer == "l":
        tries += 1  # tries = tries + 1
