# Function to read student data and create dictionary
def create_student_dict(n):
    student_dict = {}

    for _ in range(n):
        roll_number = input("Enter roll number: ")
        try:
            marks = float(input(f"Enter marks for roll number {roll_number}: "))
            student_dict[roll_number] = marks
        except ValueError:
            print("Invalid marks entered. Please enter a numeric value for marks.")

    return student_dict

# Main program
try:
    n = int(input("Enter the number of students: "))
    student_dict = create_student_dict(n)

    # Display the dictionary
    print("Student Dictionary (Roll Number: Marks):")
    print(student_dict)

except ValueError:
    print("Invalid input. Please enter a valid number for the number of students.")
