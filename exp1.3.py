def grossSalary():
    try:
        bs = float(input("Enter Basic Salary : "))
        if bs<0:
            print("Basic salary cannot be negetive.")
            return
        da = (bs * 70) / 100#da means dearness allowance
        ta =  (bs * 30) / 100#ta means travel allowance
        hra = (bs * 10) / 100#hra means house rent allowance

        grossSal = bs + da + ta + hra

        print(f"Gross Salary: {grossSal:.2f}")
    except ValueError:
        print("Please enter a valid number for the basic salary.")

grossSalary()
