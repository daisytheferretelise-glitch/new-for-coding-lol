from datetime import date ,time , datetime



today = date.today()
now= datetime.now()
print("Bob  says todays date is", today)
print("Bob says  the \nCurrent date and time is",now)

print("Bob comlains about \nDate components",today.year, today.month, today.day)