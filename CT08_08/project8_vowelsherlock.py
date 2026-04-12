 try:
    # Task 1
    with open("sherlock.txt", "r") as file:
        content = file.read()
        print("=== File Content ===")
        print(content)

    # Task 2
    total_characters = len(content)
    print("\nTotal number of characters:", total_characters)

    # Task 3
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    total_vowels = 0

    for char in content.lower():
        if char in vowels:
            vowel_counts[char] += 1
            total_vowels += 1

    print("\nVowel counts:")
    for v in vowel_counts:
        print(f"{v}: {vowel_counts[v]}")

    print("Total vowels:", total_vowels)

    # Task 4
    if total_characters > 0:
        percentage = (total_vowels / total_characters) * 100
    else:
        percentage = 0

    print(f"\nPercentage of vowels: {percentage:.2f}%")

    # Task 5: Save results to a file
    with open("vowel_counts.txt", "w") as output_file:
        output_file.write("Vowel Counts:\n")
        for v in vowel_counts:
            output_file.write(f"{v}: {vowel_counts[v]}\n")
        output_file.write(f"\nTotal vowels: {total_vowels}\n")
        output_file.write(f"Percentage of vowels: {percentage:.2f}%\n")

    print("\nResults saved to 'vowel_counts.txt' successfully.")
except FileNotFoundError:
print("Error: 'sherlock.txt' file not found.")