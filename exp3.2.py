num = int(input("Enter a number: "))

if num < 0:
    print("Number can't be negetive.")
    exit()
else:
    fact = 1
    for i in range(1,num+1):
        fact*=i
    print(f"The factorial of the number {num} is {fact}")