books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4": "BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")



if action == "B":
    if book_id in books:
        if books[book_id] == "AVAILABLE":
            books[book_id] = "BORROWED"
            print("You have borrowed the book.")
        else:
            print("The book is already borrowed.")
    else:
        print("Invalid book ID.")

elif action == "R":
    if book_id in books:
        if books[book_id] == "BORROWED":
            books[book_id] = "AVAILABLE"
            print("You have returned the book.")
        else:
            print("The book is already available.")
    else:
        print("Invalid book ID.")

else:
    print("Invalid action.")