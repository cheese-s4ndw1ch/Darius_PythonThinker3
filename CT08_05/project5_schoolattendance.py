## Task 1: Create Student Database
# **Create the Initial Attendance Database​**

# - Create a dictionary to store the names of students and their attendance records.​
# - Initialize a dictionary where each key is a student’s name, and the value is a list of booleans representing attendance ​
# - (True for present, False for absent).​
# - This dictionary will serve as the database for all subsequent tasks.


# ## Task 2: Take Student Attendance
# **Take Attendance​**

# Create a function called take_attendance()​

# Params:​
# - dictionary containing the student name and previous attendance​

# Function purpose:​
# - Loop through all the students, and ask if the student present or absence, and update the attendance accordingly.​
# - You must validate the input.​

# Return:​

attendance_db = {
    "Alice": [True, True, False, True],
    "Bob": [True, False, False, True],
    "Charlie": [True, True, True, True],
    "Diana": [False, True, True, False]
}


print(attendance_db)

def take_attendance(attendance_db):
    
    for student in attendance_db:
        while True:
            status = input(f"Is {student} present? (yes/no): ").strip().lower()

            if status in ("yes", "y"):
                attendance_db[student].append(True)
                break
            elif status in ("no", "n"):
                attendance_db[student].append(False)
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    return attendance_db
## Task 3: Calculate Attendance Percentage
# **Create a function called attendance_percentage()​**

# Params:​
# - student: String – containing the student name​
# - attendance_dict: Dictionary – containing the class names and attendance​

# Function purpose:​
# - Lookup the student in the dictionary.​
# - Calculate the percentage of True values.​
# - Return the percentage of True values​

# Return:​
# - attendance_percentage: Float – containing the attendance percentage.


#Task 4

def notify_low_attendance(attendance_db, threshold):
    low_attendance_students = []

    for student, records in attendance_db.items():
        if len(records) == 0:
            continue  # Avoid division by zero
        
        attendance_percentage = (sum(records) / len(records)) * 100
        
        if attendance_percentage < threshold:
            low_attendance_students.append(student)

    return low_attendance_students

#Task 5
def view_attendance(attendance_db):
    if not attendance_db:
        print("No attendance records available.")
        return

    for student, records in attendance_db.items():
        if len(records) == 0:
            percentage = 0
        else:
            percentage = (sum(records) / len(records)) * 100

        print(f"{student}: {percentage:.2f}% attendance")
        

## Task 5: Create the Menu System
# **Build an interactive menu to access the attendance system's features.**​

# Display a menu with the following options:​
# - 1: Take Attendance​
# - 2: Calculate Attendance Percentage for a Student​
# - 3: Notify Low Attendance​
# - 4: Exit Program​

# Based on the user’s choice:​
# - Call the respective function with the necessary inputs.​
# - Display the results of the chosen action

