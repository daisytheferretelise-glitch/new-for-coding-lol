import calendar

print("Calendar Module Project")
print("------------------------")

year = int(input("Enter a year (e.g., 2026): "))
month = int(input("Enter a month (1-12): "))

print("\nHere is the calendar for the month:")
print(calendar.month(year, month))

show_year = input("Do you want to see the full year calendar? (yes/no): ").strip().lower()

if show_year == "yes":
    print("\nFull Year Calendar:")
    print(calendar.calendar(year))

if calendar.isleap(year):
    print(f"\n{year} is a leap year.")
else:
    print(f"\n{year} is not a leap year.")
