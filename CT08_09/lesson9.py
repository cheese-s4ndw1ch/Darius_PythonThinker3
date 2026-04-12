import string

try:
    # Task 1: Open and read the file
    with open("encrypted_note.txt", "r") as file:
        content = file.read()
        print("=== Original Content ===")
        print(content)

    # Task 2: Remove punctuation and convert to lowercase
    cleaned = ""
    for char in content:
        if char not in string.punctuation:
            cleaned += char.lower()

    print("\n=== Cleaned Content ===")
    print(cleaned)

    # Task 3: Decode the message
    # Example pattern: take every 2nd character
    decoded_message = cleaned[::2]

    print("\n=== Decoded Message ===")
    print(decoded_message)

    # Task 4: Save reversed decoded message
    reversed_message = decoded_message[::-1]

    with open("hidden_message.txt", "w") as file:
        file.write(reversed_message)

    print("\nSecret saved to 'hidden_message.txt' successfully.")

except FileNotFoundError:
    print("ERROR: The encrypted note has vanished. Is someone trying to hide the truth?")