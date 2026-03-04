fruits = ["apple", "banana", "mango", "orange"]

print("Original list:", fruits)

fruits.append("grape")
print("After append:", fruits)

fruits.insert(1, "kiwi")
print("After insert:", fruits)

fruits.remove("mango")
print("After remove:", fruits)

popped = fruits.pop()
print("After pop:", fruits)
print("Popped item:", popped)

print("First item:", fruits[0])
print("Last two items:", fruits[-2:])

fruits.sort()
print("Sorted list:", fruits)

fruits.reverse()
print("Reversed list:", fruits)
