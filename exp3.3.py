num = int(input("Enter the number: "))

if num == 1:
    print("Number is neither prime nor composite.")
else:
    Flag = False
    # 3. Check for factors from 2 up to num-1
    for i in range(2, num):
        if num % i == 0:
            Flag = True
            break
            
    # 4. Final output logic
    if not Flag:
        print(f"The accepted number {num} is prime")
    else:
        print(f"The accepted number {num} is composite")