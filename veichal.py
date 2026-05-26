class BMW:
    def start(self):
        return "BMW starts with a smooth purr."

    def stop(self):
        return "BMW stops with soft braking."

class Ferrari:
    def start(self):
        return "Ferrari roars to life with a loud engine!"

    def stop(self):
        return "Ferrari stops with high‑performance brakes."

# polymorphism demonstration
def test_drive(vehicle):
    print(vehicle.start())
    print(vehicle.stop())
    print("-" * 40)

# create objects
bmw_car = BMW()
ferrari_car = Ferrari()

# run polymorphism
for car in (bmw_car, ferrari_car):
    test_drive(car)
