import pdb

def calculate_average_even(numbers):
    sm = 0
    count = 0

    for num in numbers:
        if num % 2 == 0:
            sm += num   
            count += 1

    # handle division by zero safely 
    if count == 0:
        return 0  # or raise ValueError("No even numbers found")
    
    avg = sm / count
    return avg


def main():
    numbers = [1, 3, 5, 7, 9]

    print("Calculating average of even numbers...")

    pdb.set_trace()  # Debug here if needed

    average = calculate_average_even(numbers) 
    print(f"Average of even numbers: {average}")


if __name__ == "__main__":
    main()