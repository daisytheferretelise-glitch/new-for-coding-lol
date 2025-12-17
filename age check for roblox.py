# Program to check if the entered age is between 10 and 20 years

def is_age_between_10_and_20(age):
    """Check if age is between 10 and 20 inclusive."""
    return 10 <= age <= 20

def main():
    try:
        # Take user input
        age_input = input("Enter your age: ").strip()

        # Validate if input is an integer
        if not age_input.isdigit():
            print("Invalid input. Please enter a positive integer.")
            return

        age = int(age_input)

        # Check for negative or unrealistic ages
        if age < 0 or age > 150:
            print("Invalid age. Please enter a realistic age between 0 and 150.")
            return

        # Check if age is between 10 and 20
        if is_age_between_10_and_20(age):
            print("Your age is between 10 and 20 years.")
        else:
            print(" Your age is NOT between 10 and 20 years.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
