def menu_system():
    while True:
        print("\n===== Personal Planner =====")
        print("1. Create a new task file")
        print("2. View all tasks")
        print("3. Add a new task")
        print("4. Delete a task")
        print("5. Mark a task as done")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("You chose: Create a new task file")
          

        elif choice == "2":
            print("You chose: View all tasks")
            # viewing

        elif choice == "3":
            print("You chose: Add a new task")
            #adding

        elif choice == "4":
            print("You chose: Delete a task")
            # deleting

        elif choice == "5":
            print("You chose: Mark a task as done")
            # marking

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



menu_system()