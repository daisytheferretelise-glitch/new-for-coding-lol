class Ferret:
    species="mamamal"

    def __init__(self,name,age):
        self.name=name
        self.age=age

Caramel=Ferret("Caramel",2)
Cheese=Ferret("Cheese",13)

print("Caramel is a {}".format(Caramel.species) )
print("Cheese is a {}".format(Cheese.species) )

print("{} is {} years old".format(Caramel.name, Caramel.age) )
print("{} is {} years old".format(Cheese.name, Cheese.age) )