try:
    number=int(input("Enter a number: "))
    print("The number enterd is",number)

except ValueError as ex:
    print("Exception: ", ex)