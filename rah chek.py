print("Bob will now check your age")
def check_age():
    try:
        age_input = input("Bob said you should enter your age: ")
        age = int(age_input)  # Try converting to integer
        if age % 2 == 0:
            print("Bob said your age is even.")
        else:
            print("Bob said your age is odd.")
    except ValueError:
        print("Bob said your input was invalid input! Please enter a whole number without letters, decimals, or symbols.")

check_age()
