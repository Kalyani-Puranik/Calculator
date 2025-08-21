class Basic:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y


def main():
    calc = Basic()

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", calc.add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", calc.subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", calc.multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", calc.divide(num1, num2))
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
