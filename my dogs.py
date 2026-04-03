class critters:
    species = "herbi familiaris"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

Bob1 = critters("ferret", "weazle")
Bob2 = critters("rabbit", "hamster")

print("Species:", Bob1.species)
print("Breed:", Bob1.breed)
print("Name:", Bob1.name)

print("Species:", Bob2.species)
print("Breed:", Bob2.breed)
print("Name:", Bob2.name)
