# Automate the process of grading a quiz,
# calculating class averages, and identifying top
# scorers.​
# ​In this activity, you will build a system to:​
# Grade all students based on their answers.​

# Calculate the average score for the class.​

# Identify the student(s) with the highest score.​

# Display all results in an organized format.​

# ​


# Predefined data
answer_key = ["A", "B", "B", "D"]  # Correct answers for the quiz
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]



#Do we want to calculate each student’s score?

#Do we want percentages?

#Do we want to find the highest score?

#Do we want to notify students who failed?

#Most common goal → compare each student’s answers to the answer key and calculate their score.

#loop thru each student + answer and compare

def grade_students(answer_key, student_answers):
    result = ""

    for student, answers in student_answers.items():
        score = 0

        for i in range(len(answer_key)):
            if answers[i] == answer_key[i]:
                score += 1

        percentage = (score / len(answer_key)) * 100
        result += f"{student}: {score}/{len(answer_key)} ({percentage:.2f}%)\n"

    return result


# Task 3
def find_highest_scorer(quiz_scores):
   
        quiz_scores (dict): Dictionary containing student names as keys
                            and scores as values.

    
        list: List of student name(s) with the highest score.
    
    if not quiz_scores:
        return []

    highest_score = max(quiz_scores.values())
    highest_scorers = [name for name, score in quiz_scores.items() if score == highest_score]

    return highest_scorers
#Task 4
def display_results(quiz_scores):
    
    if not quiz_scores:
        print("No quiz results to show.")
        return

    print("\n--- Class Results ---")
    for student, score in quiz_scores.items():
        print(student, "scored", score)
    print("---------------------")


    def menu_system():
    quiz_scores = {}  
    while True:
        print("\n===== Quiz Score Menu =====")
        print("1. Add or Update Student Score")
        print("2. Display All Results")
        print("3. Find Highest Scorer(s)")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            score_input = input("Enter student score: ")

            
            try:
                score = float(score_input)
                quiz_scores[name] = score
                print("Score saved successfully!")
            except ValueError:
                print("Please enter a valid number for the score.")

        elif choice == "2":
            display_results(quiz_scores)

        elif choice == "3":
            highest = find_highest_scorer(quiz_scores)

            if highest:
                print("\nHighest Scorer(s):")
                for student in highest:
                    print(student)
            else:
                print("No scores available yet.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")



menu_system()