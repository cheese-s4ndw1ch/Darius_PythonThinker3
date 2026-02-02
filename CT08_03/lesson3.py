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
    # this should be outside the loop if you would like to have different question.
    # suggestion would be to stick to one question to understand the flow
    order = input("What would you like to order? ").lower()

    # this should be outside the loop if you decide to have a second question
    # this should be after the exit condition.
    if order in menu:
        print(f"{order} costs ${menu[order]:.2f}")
    else:
        print("Sorry, that item is unavailable.")

    again = input("Would you like to order something else? (say no more to end): ").lower()
    # the exit condition should be one of the first thing in the loop after your question
    if again == "no more":
        print("Thank you! Have a great day!")


        print("\n🧾 Your Order Summary")
        print("--------------------")
    
    # task 3 can be written here:
    # task 3 need to be in another while loop because if did not type y or n, it will need to be repeated

    # in the part whereby the customer answer yes
    # need to add them into the customer order
    # to add to customer order, need to check if the order exist
    # if exist 
    #     need to retrieve from customer order and add the unit price and assign back
    #     i.e. customer_order[order] += stuff[order]
    # else
    #     customer_order[order] = stuff[order]
    

    #should this be in the while loop or outside the while loop? 
    if customer_order:
        # this part is ok for the order summary
        for item, price in customer_order.items():
            print(f"{item.title()} - ${price:.2f}")
    else:
        print("You did not order anything.")

    print("Thank you for visiting! 😊")

    # this will break the code after the second qns
    break

# this is the output i have triedWhat would you like to order? burger
# burger costs $8.99
# Would you like to order something else? (say no more to end): burger
# You did not order anything.
# Thank you for visiting! 😊