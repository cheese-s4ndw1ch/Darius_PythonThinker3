# Qns: Student Results File Processing

# You are given a text file called results.txt.
# Each line contains a student's name and mark, separated by a space.

# Example:
# Alex 92
# Ben 43
# Clara 78

# Your task:

# 1. Read the data from results.txt.

# 2. Convert the data into a dictionary called student_results.
#    The name should be the key.
#    The mark should be the value.

# 3. With the dictionary, create another dictionary that count the student in the follow range:
# 0 - 50, 51 - 70, 71 - 90, 91 - 100

# 4. Do a analysis of the score to get the following and print it to a output txt file 
# Min score: 
# Max Score:
# No of people in each range
# 0 - 50:  people
# 51 - 70: people
# 71 - 90: people
# 91 - 100: people
# the mode for range: __________
# average score:
#T1 and 2
student_results = {}

try:
    with open("results.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            mark = int(parts[1])
            student_results[name] = mark


#T3
range_count = {
    "0-50": 0,
    "51-70": 0,
    "71-90": 0,
    "91-100": 0
}

for mark in student_results.values():
    if 0 <= mark <= 50:
        range_count["0-50"] += 1
    elif 51 <= mark <= 70:
        range_count["51-70"] += 1
    elif 71 <= mark <= 90:
        range_count["71-90"] += 1
    elif 91 <= mark <= 100:
        range_count["91-100"] += 1
except FileNotFoundError:
print("ERROR: results.txt not found.")

    