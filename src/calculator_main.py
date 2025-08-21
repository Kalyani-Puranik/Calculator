from basic_ops import Basic
from logarithmic_ops import logs
from trigonometric_ops import trigz

def main():
    while True:
        print("\n<3 Main Calculator Menu <3")
        print("1. Basic Calculator")
        print("2. Logarithmic Calculator")
        print("3. Trigonometric Calculator")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            basic_calc = Basic()

        elif choice == "2":
            log_calc = logs()
            

        elif choice == "3":
            trig_calc = trigz()

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
    main()
