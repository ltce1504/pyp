import math

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle "))
    area = math.pi * radius ** 2 
    print(f"The area of the cicle is: {area:.2f}")
    
def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle "))
    width = float(input("Enter the width ofd the rectangle "))
    area = length * width 
    print(f"The area of the rectangle is: {area:.2f}")

def calculate_traingle_area():
    base = float(input("Enter the base of the triangle "))
    height = float(input("Enter the height of the triangle "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area:.2f}")

def main():
    while True:
        print("\nChoose a geometric figure to calculate its area")
        print("1. Circle")
        print("2. Rectangle")
        print("3.Triangle")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            calculate_circle_area()
        elif choice == '2':
            calculate_rectangle_area()
        elif choice == '3':
            calculate_traingle_area()
        elif choice == '4':
            print("Exiting the program Goodbye. ")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
"""this means that the code inside this block will only be
 executed if the script is run directly, and not when 
 it is imported as a module in another script
 which means the commans - __name__ == "__main__"."""
