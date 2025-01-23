import art

print(art.logo)

# Operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def mod(n1, n2):
    return n1 % n2

# Operation dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": mod
}

# Calculator function
def calculator():
    history = []  # List to store operation history
    num1 = float(input("Enter the first number: "))

    while True:
        print("Operations: ")
        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation! Please choose a valid one.")
            continue

        try:
            num2 = float(input("Enter the next number: "))
        except ValueError:
            print("Invalid number! Please enter a valid number.")
            continue
        
        # Perform calculation and add to history
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        history.append(f"{num1} {operation_symbol} {num2} = {result}")

        # Ask user to continue or exit
        choice = input(f"Type 'y' to continue with {result}, 'n' to start a new calculation, or 'exit' to quit: ").lower()
        
        if choice == "y":
            num1 = result  # Continue with the result
        elif choice == "n":
            num1 = float(input("Enter a new first number: "))
        elif choice == "exit":
            print("Calculator closed.")
            print("Operation history:")
            for entry in history:
                print(entry)
            break  # Exit the calculator
        else:
            print("Invalid option! Please type 'y', 'n', or 'exit'.")
            
calculator()
