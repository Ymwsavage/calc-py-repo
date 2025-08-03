def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Input first number
    first_number = float(input("Enter the first number: "))
    
    # Input second number
    second_number = float(input("Enter the second number: "))
    
    # Input operation
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
   
    operation = input("Enter the number corresponding to the operation (1-4): ")

    # Perform the chosen operation
    if operation == '1':
        result = first_number + second_number
        print(f"The result of {first_number} + {second_number} = {result}")
    elif operation == '2':
        result = first_number - second_number
        print(f"The result of {first_number} - {second_number} = {result}")
    elif operation == '3':
        result = first_number * second_number
        print(f"The result of {first_number} * {second_number} = {result}")
    elif operation == '4':
        if second_number != 0:
            result = first_number / second_number
            print(f"The result of {first_number} / {second_number} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation selected. Please choose a valid operation.")

def main():
    while True:
        calculator()
        play_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
