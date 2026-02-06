import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date bettween", startDate, "and", endDate)
    randomGenorater= random.random()
    dateFormat ="%m/%d/%Y"

    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime=time.mktime(time.strptime(endDate,dateFormat))

    randomTime= startTime + randomGenorater *(endTime - startTime)
    randomDate= time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("Random date=", getRandomDate("11/2/2015","11/2/2026"))