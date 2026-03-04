fruits = {"apple", "banana", "mango", "orange"}

print("Original set:", fruits)

fruits.add("grape")
print("After add:", fruits)

fruits.update(["kiwi", "melon"])
print("After update:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

popped = fruits.pop()
print("After pop:", fruits)
print("Popped item:", popped)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric difference:", a ^ b)
