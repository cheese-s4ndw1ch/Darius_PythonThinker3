stationary = {
    "school bag": 60,
    "Pencil": 0.50,
    "Notebook": 2.50,
    "Ruler": 1.50,
    "Calculator": 30,
    "Eraser": 0.12,
    "Writing Pad": 2.50
}

# suggest the above to be in all lower case

# Dictionary to store customer's order
order = {}

print("Welcome to the Bookshop!")
print("Available items:\n")

for item, price in stationary.items():
    #item here can use .title() so that the first leter of each word will be upper case
    print(f"{item}: ${price:.2f}")

while True:
    # the reason for the key to be in lower case is for easier checking when you have the input with .lower().strip()
    # it force all upper case input by user to be lower case and remove the white space accidentally type by user
    choice = input("\nEnter the item you want to order (or type 'no more' to stop): ")

    if choice.lower() == "no more":
        break

    elif choice in stationary:
        print(f"{choice} costs ${stationary[choice]:.2f}")
        add_item = input("Would you like to add this item to your order? (yes/no): ")

        # suggest to put another while loop here to ask the user to input y or no if they did not
        if add_item.lower() == "yes":
            # check if the item is already in order
            # if the choice exist, it will overwrite instead of adding the unit price onto it
            # hence there should be condition to check if choice in order
            # if choice in order
            #     order[choice] += stationary[choice]
            # else
            order[choice] = stationary[choice] # this is ok if the choice does not exist
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

# try to do the BOS challenge 1 and 2
# to help you to understand nested loops

## Challenge 1: Track Quantities of Items
# Allow the customer to specify how many of each item they want to buy.​
# Store both the item and quantity in a nested dictionary.​
# - purchases = ​{"Notebook": {"quantity": 2, "cost": 5.00}}​
# Calculate the total cost based on quantities.

# ## Challenge 2: Apply Discounts
# The goal of this challenge is to introduce a discount system to your program, allowing customers to receive a percentage discount if their total spending exceeds a certain threshold.​
# - Example: If the customer spends more than $20, they get a 10% discount on their bill.