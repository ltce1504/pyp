def create_student_database():
    return{}

def add_update_student(database, student_name, grades, attendance_percentage):

    database[student_name] = {
        'grades' : grades,
        'attendance' : attendance_percentage
    }
    print(f"Record for {student_name} has been added/updated. ")

def calculate_average_grade(grades):

    if not grades:
        return 0
    return sum(grades) / len(grades)

def display_student_records(database):

    print("\n--- Students Records ---")
    if not database:
        print("No Records found.")
        return

    for name, data in database.items():
        average_grade = calculate_average_grade(data['grades'])
        print(f"\nName: {name}")
        print(f"\nGrades : {data['grades']}")
        print(f"\nAverage Grade : {average_grade: .2f} ")
        print(f"\nAttendance : {data['attendance']}% ")
    print(f"------------------------------\n")

if __name__ == "__main__":
    student_db = create_student_database()

    add_update_student(student_db, "Ram", [90, 80, 92], 95.0)
    add_update_student(student_db, "Shaam", [75, 86, 70], 88.5)

    display_student_records(student_db)

    student_db["Ram"]["grades"].append(94)
    print("Updated Ram's grades manually.")

    add_update_student(student_db, "Harry", [100, 99], 100.0)

    display_student_records(student_db)


""" 
hers's the logic behind the code:
1. We start by creating an empty student database using the `create_student_database` function, which returns an empty dictionary.
2. We then add or update student records using the `add_update_student` function. 
This function takes the database, student name, grades, and attendance percentage as parameters and updates the database accordingly.
3. The `calculate_average_grade` function computes the average grade for a list of grades.
4. The `display_student_records` function prints out all the student records in a readable format,
including their average grade and attendance percentage.
5. In the main block, we demonstrate the functionality by adding/updating student records and displaying
 them before and after making manual updates to a student's grades.
 This code provides a simple way to manage student records, allowing for easy addition, updating, and display of student information.
 """