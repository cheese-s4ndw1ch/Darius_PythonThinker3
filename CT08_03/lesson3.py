menu = {
    "burger": 8.99,
    "pizza": 10.50,
    "pasta": 9.25,
    "salad": 6.75,
    "soda": 2.50
}

print("Restaurant Menu")

for item, price in menu.items():
    print(f"{item} - ${price:.2f}")

print("\n")
customer_order = {}

while True:
    order = input("What would you like to order? ").lower()

    if order in menu:
        print(f"{order} costs ${menu[order]:.2f}")
    else:
        print("Sorry, that item is unavailable.")

    again = input("Would you like to order something else? (say no more to end): ").lower()
    if again == "no more":
        print("Thank you! Have a great day!")


        print("\n🧾 Your Order Summary")
        print("--------------------")
    if customer_order:
        for item, price in customer_order.items():
            print(f"{item.title()} - ${price:.2f}")
    else:
        print("You did not order anything.")

    print("Thank you for visiting! 😊")

    break
        dw