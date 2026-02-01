stationary = {
    "school bag": 60,
    "Pencil": 0.50,
    "Notebook": 2.50,
    "Ruler": 1.50,
    "Calculator": 30,
    "Eraser": 0.12,
    "Writing Pad": 2.50
}

# Dictionary to store customer's order
order = {}

print("Welcome to the Bookshop!")
print("Available items:\n")

for item, price in stationary.items():
    print(f"{item}: ${price:.2f}")

while True:
    choice = input("\nEnter the item you want to order (or type 'no more' to stop): ")

    if choice.lower() == "no more":
        break

    elif choice in stationary:
        print(f"{choice} costs ${stationary[choice]:.2f}")
        add_item = input("Would you like to add this item to your order? (yes/no): ")

        if add_item.lower() == "yes":
            # check if the item is already in order
            order[choice] = stationary[choice]
            print(f"{choice} has been added to your order.")
        else:
            print(f"{choice} was not added to your order.")
        # if they give you anything beside yes and no, you need to check to ask them give you the correct one
    else:
        print("Sorry, that item is unavailable.")

# Order summary and total cost
print("\n--- Order Summary ---")

total_cost = 0

if order:
    for item, price in order.items():
        print(f"{item}: ${price:.2f}")
        total_cost += price

    print(f"\nTotal Cost: ${total_cost:.2f}")
else:
    print("You did not order any items.")

print("\nThank you for shopping with us!")