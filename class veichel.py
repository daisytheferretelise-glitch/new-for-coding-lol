class vehicle :
    def __init__(self,max_speed,mileage):
        self.max_speed =max_speed
        self.mileage=mileage

modelX=vehicle(100,10)

print("Model X Max_speed",modelX.max_speed)
print("Model x Mileage",modelX.mileage)