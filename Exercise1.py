import tkinter as tk
import random

def displayMenu():
    # Hide other frames (quiz, results)
    difficulty_frame.pack_forget()
    question_frame.pack_forget()
    result_frame.pack_forget()
    
    menu_frame.pack(pady=50)


def startQuiz(difficulty):
    global score, question_num, difficulty_level
    score = 0
    question_num = 0
    difficulty_level = difficulty

    menu_frame.pack_forget()
    difficulty_frame.pack_forget()

    question_frame.pack()

    nextProblem(difficulty)

# Function to generate a random integer based on the difficulty level
def randomInt(difficulty):
    if difficulty == 1:  # Easy: single digits
        return random.randint(1, 9)
    elif difficulty == 2:  # Moderate: double digits
        return random.randint(10, 99)
    elif difficulty == 3:  # Advanced: 4-digit numbers
        return random.randint(1000, 9999)

# Function to randomly decide if the operation is addition or subtraction
def decideOperation():
    return random.choice(['+', '-'])

# Function to display the next problem
def nextProblem(difficulty):
    global num1, num2, operation, correct_answer, question_num
    if question_num >= 10:
        displayResults()
        return
    
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()
    
    # Update the problem text
    problem_label.config(text=f"{num1} {operation} {num2} = ")
    user_answer_entry.delete(0, tk.END)  # Clear previous answer
    correct_answer = num1 + num2 if operation == '+' else num1 - num2
    question_num += 1

# Function to check if the user's answer is correct and update the score
def checkAnswer():
    global score
    try:
        user_answer = int(user_answer_entry.get())
        if user_answer == correct_answer:
            score += 10  # Correct on the first attempt
            nextProblem(difficulty_level)
        else:
            # Allow a second attempt
            second_attempt_label.pack()
            second_answer_entry.pack()
            submit_second_button.pack()
            submit_button.config(state=tk.DISABLED)  # Disable the first submit button
    except ValueError:
        pass 

def checkSecondAnswer():
    global score
    try:
        second_answer = int(second_answer_entry.get())
        if second_answer == correct_answer:
            score += 5  
        nextProblem(difficulty_level)
    except ValueError:
        pass

def displayResults():
    
    question_frame.pack_forget()
    
    
    result_frame.pack()

    result_label.config(text=f"Your final score is: {score}/100")
    
    if score >= 90:
        grade_label.config(text="Grade: A+")
    elif score >= 80:
        grade_label.config(text="Grade: A")
    elif score >= 70:
        grade_label.config(text="Grade: B")
    elif score >= 60:
        grade_label.config(text="Grade: C")
    else:
        grade_label.config(text="Grade: F")
    
    # Ask if the user wants to play again
    play_again_button.pack()

def playAgain():
    result_frame.pack_forget()  
    displayMenu()  


root = tk.Tk()
root.title("Math Quiz")


difficulty_level = 1
score = 0
question_num = 0
num1 = 0
num2 = 0
operation = ''
correct_answer = 0

# Menu Frame (difficulty selection)
menu_frame = tk.Frame(root)
menu_label = tk.Label(menu_frame, text="DIFFICULTY LEVEL\n1. Easy\n2. Moderate\n3. Advanced", font=("Arial", 16))
menu_label.pack(pady=20)

easy_button = tk.Button(menu_frame, text="Easy", font=("Arial", 14), command=lambda: startQuiz(1))
easy_button.pack(pady=5)

moderate_button = tk.Button(menu_frame, text="Moderate", font=("Arial", 14), command=lambda: startQuiz(2))
moderate_button.pack(pady=5)

advanced_button = tk.Button(menu_frame, text="Advanced", font=("Arial", 14), command=lambda: startQuiz(3))
advanced_button.pack(pady=5)

menu_frame.pack(pady=50)

# Difficulty Frame
difficulty_frame = tk.Frame(root)
back_button = tk.Button(difficulty_frame, text="Back to Menu", font=("Arial", 14), command=displayMenu)
back_button.pack()

# Question Frame
question_frame = tk.Frame(root)

problem_label = tk.Label(question_frame, text="", font=("Arial", 16))
problem_label.pack(pady=20)

user_answer_entry = tk.Entry(question_frame, font=("Arial", 16))
user_answer_entry.pack(pady=10)

submit_button = tk.Button(question_frame, text="Submit Answer", font=("Arial", 14), command=checkAnswer)
submit_button.pack(pady=10)

second_attempt_label = tk.Label(question_frame, text="Incorrect, try again.", font=("Arial", 14), fg="red")
second_attempt_label.pack_forget()

second_answer_entry = tk.Entry(question_frame, font=("Arial", 16))
second_answer_entry.pack_forget()

submit_second_button = tk.Button(question_frame, text="Submit Second Answer", font=("Arial", 14), command=checkSecondAnswer)
submit_second_button.pack_forget()

# Result Frame
result_frame = tk.Frame(root)

result_label = tk.Label(result_frame, text="", font=("Arial", 16))
result_label.pack(pady=20)

grade_label = tk.Label(result_frame, text="", font=("Arial", 16))
grade_label.pack(pady=10)

play_again_button = tk.Button(result_frame, text="Play Again", font=("Arial", 14), command=playAgain)
play_again_button.pack(pady=20)

# Start the GUI
displayMenu()  # Show the initial menu

# Run the Tkinter event loop
root.mainloop()
