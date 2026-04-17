#program : listmanager
#Sample data : List of students enrolled in various entrance

students_CET = set(["Vishal","Rohan","Jay","David","Eva","Pooja","Dev"])
students_JEE = set(["Vishal","Jay","Kiran","Pooja","Hena","Ivy"])
students_NEET = set(["David","Eva","Jay","Kiran","Neha","Vishal"])

def union_students():
    union_students = students_CET.union(students_JEE,students_NEET)
    print("Students enrolled in at least one exam (union): ")
    print(union_students)

def intersection_students():
    intersection_students = students_CET.intersection(students_JEE,students_NEET)
    print("\nStudents enrolled  in all three exams (Intersection): ")
    print(intersection_students)

def difference_students():
    only_CET_students = students_CET.difference(students_JEE,students_NEET)
    print("\nStudents enrolled only in CET (Difference): ")
    print(only_CET_students)

while True:
    print("\nMenu")
    print("1.Union")
    print("2.Intersection")
    print("3.Difference")
    print("4. Exit")

    n = int(input("Enter your choice : "))

    if n == 1:
        union_students()
    elif n == 2:
        intersection_students()
    elif n== 3:
        difference_students()
    elif n == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
        break

This program demonstrates the use of set operations to manage and analyze data about students enrolled in different entrance exams. 
It allows users to easily find out which students are enrolled in which exams, and how they overlap.
 The use of sets simplifies the logic for these operations, making the code more efficient and easier to read."""

