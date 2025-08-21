import math
class trigz:
    def sin_of(self, x):
        try:
            return math.sin(x)
        except Exception as e:
            return f"Error: {e}"

    def cos_of(self, x):
        try:
            return math.cos(x)
        except Exception as e:
            return f"Error: {e}"

    def tan_of(self, x):
        try:
            return math.tan(x)
        except Exception as e:
            return f"Error: {e}"

    def cosec_of(self, x):
        try:
            if math.sin(x) == 0:
                return "Error: cosec undefined (sin(x) = 0)."
            return 1 / math.sin(x)
        except Exception as e:
            return f"Error: {e}"

    def sec_of(self, x):
        try:
            if math.cos(x) == 0:
                return "Error: sec undefined (cos(x) = 0)."
            return 1 / math.cos(x)
        except Exception as e:
            return f"Error: {e}"

    def cot_of(self, x):
        try:
            if math.tan(x) == 0:
                return "Error: cot undefined (tan(x) = 0)."
            return 1 / math.tan(x)
        except Exception as e:
            return f"Error: {e}"

    def inv_sin_of(self, x):
        try:
            return math.asin(x)
        except ValueError:
            return "Error: domain of asin is [-1, 1]."
        except Exception as e:
            return f"Error: {e}"

    def inv_cos_of(self, x):
        try:
            return math.acos(x)
        except ValueError:
            return "Error: domain of acos is [-1, 1]."
        except Exception as e:
            return f"Error: {e}"

    def inv_tan_of(self, x):
        try:
            return math.atan(x)
        except Exception as e:
            return f"Error: {e}"

    def main(self):
        calc = trigz()

        while True:
            print("\n--- Trigonometric Calculator ---")
            print("1. sin(x)")
            print("2. cos(x)")
            print("3. tan(x)")
            print("4. cosec(x)")
            print("5. sec(x)")
            print("6. cot(x)")
            print("7. inv_sin(x)  [inverse sin]")
            print("8. inv_cos(x)  [inverse cos]")
            print("9. inv_tan(x)  [inverse tan]")
            print("10. Exit")

            choice = input("Enter your choice (1-10): ")

            try:
                if choice in ["1", "2", "3", "4", "5", "6"]:
                    x = float(input("Enter angle in radians: "))

                    if choice == "1":
                        print("Result:", calc.sin_of(x))
                    elif choice == "2":
                        print("Result:", calc.cos_of(x))
                    elif choice == "3":
                        print("Result:", calc.tan_of(x))
                    elif choice == "4":
                        print("Result:", calc.cosec_of(x))
                    elif choice == "5":
                        print("Result:", calc.sec_of(x))
                    elif choice == "6":
                        print("Result:", calc.cot_of(x))

                elif choice in ["7", "8", "9"]:
                    x = float(input("Enter a number: "))

                    if choice == "7":
                        print("Result (radians):", calc.asin_of(x))
                    elif choice == "8":
                        print("Result (radians):", calc.acos_of(x))
                    elif choice == "9":
                        print("Result (radians):", calc.atan_of(x))

                elif choice == "10":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice! Please try again.")

            except ValueError:
                print("Invalid input! Please enter a valid number.")
            except Exception as e:
                print(f"Unexpected error: {e}")


if __name__ == "__main__":
    trigz().main()
