
#Task 1
def caesar_shift_character(char, key, mode):
    ascii_val = ord(char)

  
    if ascii_val < 32 or ascii_val > 126:
        return char

    if mode == "decrypt":
        key = -key

    
    shifted = (ascii_val - 32 + key) % 95 + 32

    return chr(shifted)

 #Task 2

def caesar_shift_sentence(sentence, key, mode):
    result = ""

    for char in sentence:
        result += caesar_shift_character(char, key, mode)

    return result
#Task 3
def caesar_shift_list(sentences, key, mode):
    result = []

    for sentence in sentences:
        shifted_sentence = caesar_shift_sentence(sentence, key, mode)
        result.append(shifted_sentence)

    return result


def caesar_shift_file(input_filename, output_filename, key, mode):
    try:
        with open(input_filename, "r") as infile:
            lines = infile.readlines()

        shifted_lines = []

        for line in lines:
            shifted_line = caesar_shift_sentence(line, key, mode)
            shifted_lines.append(shifted_line)

        with open(output_filename, "w") as outfile:
            outfile.writelines(shifted_lines)

        print("File processed successfully!")

    except FileNotFoundError:
        print("ERROR: File not found.")
#Task 4

def caesar_shift_file(input_filename, output_filename, key, mode):
    try:
        with open(input_filename, "r") as infile:
            lines = infile.readlines()

        shifted_lines = []

        for line in lines:
            shifted_line = caesar_shift_sentence(line, key, mode)
            shifted_lines.append(shifted_line)

        with open(output_filename, "w") as outfile:
            outfile.writelines(shifted_lines)

        print("File processed successfully!")

    except FileNotFoundError:
        print("ERROR: File not found.")

#Task 5

def brute_force_decrypt(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        for key in range(95):  
            print(f"\nKey = {key}")
            decrypted = caesar_shift_sentence(content, key, "decrypt")
            print(decrypted)

    except FileNotFoundError:
        print("ERROR: File not found.")

   
