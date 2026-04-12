import random
import string

# Task 1: Generate strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    # Ensure at least one of each required type
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    # Fill remaining length
    for _ in range(length - 4):
        password += random.choice(characters)

    # Shuffle password
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)


# Task 2: Create new user
def create_new_user(user_db):
    username = input("Enter new username: ")

    if username in user_db:
        print("Username already exists.")
    else:
        password = generate_password(12)
        user_db[username] = password
        print(f"User created!\nUsername: {username}\nPassword: {password}")

    return user_db


# Task 3: Update password
def update_password(user_db):
    username = input("Enter username: ")

    if username not in user_db:
        print("User not found.")
        return user_db

    current_password = input("Enter current password: ")

    if user_db[username] == current_password:
        new_password = generate_password(12)
        user_db[username] = new_password
        print(f"Password updated!\nUsername: {username}\nNew Password: {new_password}")
    else:
        print("Incorrect password.")

    return user_db


# Task 4: Login
def login(user_db):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in user_db and user_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Login failed.")
        return False


# Task 5: View user data (masked)
def view_user_data(user_db):
    print("\nUser Data:")
    for username, password in user_db.items():
        masked = "*" * len(password)
        print(f"Username: {username}, Password: {masked}")


# Task 6: Menu system
def view_menu():
    user_db = {}

    while True:
        print("\n=== User Management System ===")
        print("1. Create new user")
        print("2. Update password")
        print("3. Login")
        print("4. View user data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_db = create_new_user(user_db)
        elif choice == "2":
            user_db = update_password(user_db)
        elif choice == "3":
            login(user_db)
        elif choice == "4":
            view_user_data(user_db)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run program
view_menu()