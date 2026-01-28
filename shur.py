import os

shutdown = input("Do you wish to shut down your computer? (yes or no): ").lower()

if shutdown == "yes":
    os.system("shutdown /s /t 1")
elif shutdown == "no":
    print("Shutdown cancelled.")
else:
    print("Invalid input. Please type 'yes' or 'no'.")
