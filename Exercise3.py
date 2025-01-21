file_path = "StudentMarks.txt"

# Function to load and process student marks
def load_student_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # First line gives the number of students
        num_students = int(lines[0].strip())
        student_data = []

        # Process each student's data
        for line_number, line in enumerate(lines[1:], start=2):  # Start counting from line 2
            parts = line.strip().split()

            # Validate the line format
            if len(parts) != 6:
                print(f"Warning: Line {line_number} is incorrectly formatted and will be skipped: {line.strip()}")
                continue

            try:
                student_number = int(parts[0])  # First part is the student number
                student_name = parts[1]  # Second part is the student name
                course_scores = list(map(int, parts[2:5]))  # Next three are course scores
                exam_score = int(parts[5])  # Last is the examination score

                # Calculate total marks
                total_marks = sum(course_scores) + exam_score

                # Store all data in a dictionary
                student_data.append({
                    "number": student_number,
                    "name": student_name,
                    "course_scores": course_scores,
                    "exam_score": exam_score,
                    "total_marks": total_marks,
                })
            except ValueError:
                print(f"Error: Invalid data format on line {line_number}: {line.strip()}")

        return num_students, student_data

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0, []
    except ValueError:
        print("Error: The first line of the file must be an integer indicating the number of students.")
        return 0, []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0, []

# Functions to provide the new features
def view_all_students(student_data):
    if not student_data:
        print("No student data available.")
        return
    print("All Student Records:")
    for student in student_data:
        print(f"Student Number: {student['number']}, Name: {student['name']}, Total Marks: {student['total_marks']}")

def view_individual_student(student_data):
    if not student_data:
        print("No student data available.")
        return
    try:
        student_number = int(input("Enter the student number: "))
        student = next((s for s in student_data if s['number'] == student_number), None)
        if student:
            print(f"Student Number: {student['number']}")
            print(f"  Name: {student['name']}")
            print(f"  Course Scores: {student['course_scores']}")
            print(f"  Exam Score: {student['exam_score']}")
            print(f"  Total Marks: {student['total_marks']}")
        else:
            print(f"No record found for student number {student_number}.")
    except ValueError:
        print("Invalid input. Please enter a valid student number.")

def show_highest_score(student_data):
    if not student_data:
        print("No student data available.")
        return
    highest_score_student = max(student_data, key=lambda s: s['total_marks'])
    print("Student with the Highest Total Score:")
    print(f"Student Number: {highest_score_student['number']}, Name: {highest_score_student['name']}, Total Marks: {highest_score_student['total_marks']}")

def show_lowest_score(student_data):
    if not student_data:
        print("No student data available.")
        return
    lowest_score_student = min(student_data, key=lambda s: s['total_marks'])
    print("Student with the Lowest Total Score:")
    print(f"Student Number: {lowest_score_student['number']}, Name: {lowest_score_student['name']}, Total Marks: {lowest_score_student['total_marks']}")

# Main program
def main():
    print("Student Marks Analysis")
    num_students, student_data = load_student_data(file_path)

    while True:
        print("\nOptions:")
        print("1. View all student records")
        print("2. View an individual student record")
        print("3. Show student with the highest total score")
        print("4. Show student with the lowest total score")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_all_students(student_data)
        elif choice == "2":
            view_individual_student(student_data)
        elif choice == "3":
            show_highest_score(student_data)
        elif choice == "4":
            show_lowest_score(student_data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
