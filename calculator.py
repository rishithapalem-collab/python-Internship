def add(x, y):
     return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponent(x, y):
    return x ** y


def modulus(x, y):
    return x % y


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def main():
    print("Welcome to the Python Calculator")

    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponent")
        print("6. Modulus")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Please choose a valid option from 1 to 7.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            result = add(num1, num2)
            operator = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = divide(num1, num2)
            operator = "/"
        elif choice == "5":
            result = exponent(num1, num2)
            operator = "^"
        else:
            if num2 == 0:
                print("Error: Modulus by zero is not allowed.")
                continue
            result = modulus(num1, num2)
            operator = "%"

        print(f"\n{num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    main()
