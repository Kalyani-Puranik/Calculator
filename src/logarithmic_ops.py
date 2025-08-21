import math
class logs:
    def log_of(self, x):
        try:
            return math.log10(x)
        except ValueError:
            return "Error: log is undefined for zero or negative numbers."
        except Exception as e:
            return f"Unexpected error: {e}"

    def natural_log(self, x):
        try:
            return math.log(x)  # default base = e
        except ValueError:
            return "Error: natural log is undefined for zero or negative numbers."
        except Exception as e:
            return f"Unexpected error: {e}"

    def egzponets(self, base, power):
        try:
            return math.pow(base, power)
        except Exception as e:
            return f"Unexpected error: {e}"

    def main(self):
        calc = logs()

        while True:
            print("\n--- Math Menu ---")
            print("1. Log base 10")
            print("2. Natural log (ln)")
            print("3. Exponents (base ^ power)")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                try:
                    x = float(input("Enter a number: "))
                    print("Result:", calc.log_of(x))
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            elif choice == "2":
                try:
                    x = float(input("Enter a number: "))
                    print("Result:", calc.natural_log(x))
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            elif choice == "3":
                try:
                    base = float(input("Enter base number: "))
                    power = float(input("Enter power number: "))
                    print("Result:", calc.egzponets(base, power))
                except ValueError:
                    print("Invalid input! Please enter valid numbers.")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    logs().main()
