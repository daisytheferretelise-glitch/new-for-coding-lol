class Vehicle:
    def __init__(self, fare):
        self.fare = fare

    def total_fare(self):
        return self.fare

class Bus(Vehicle):
    def __init__(self, fare, passengers):
        super().__init__(fare)
        self.passengers = passengers

    def total_fare(self):
        return self.fare * self.passengers

bus = Bus(10, 30)
print("Total Fare:", bus.total_fare())
