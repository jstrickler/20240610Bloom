
print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        print("please enter ticket quantity at the prompt...")
        continue  # Skip rest of loop; start back at top
    # if raw_quantity.lower() == 'q':
    if raw_quantity.startswith('q'):
        print("goodbye!")
        break  # Exit loop

    quantity = int(raw_quantity)  # could validate via try/except
    print(f"sending {quantity} ticket(s)")

#  obj.method(arg)   function(arg)