# calculator.py

# Define functions for operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    print("===== Simple CLI Calculator =====")
    print("Available operations: + , - , * , /")
    print("Type 'exit' to quit the program.\n")

    while True:
        choice = input("Enter operation (+, -, *, /) or 'exit': ").strip()

        if choice.lower() == "exit":
            print("Exiting calculator... Goodbye!")
            break
        if choice in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '+':
                    print("Result:", add(num1, num2))
                elif choice == '-':
                    print("Result:", subtract(num1, num2))
                elif choice == '*':
                    print("Result:", multiply(num1, num2))
                elif choice == '/':
                    print("Result:", divide(num1, num2))

            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")
        else:
            print("❌ Invalid operation! Please choose +, -, *, / or 'exit'.")

        print()  # For spacing


if __name__ == "__main__":
    calculator()
