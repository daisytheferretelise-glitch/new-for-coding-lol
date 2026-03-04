fruits = ("apple", "banana", "mango", "orange")

print("Original tuple:", fruits)

print("First item:", fruits[0])
print("Last item:", fruits[-1])

print("Slice (first two):", fruits[:2])

print("Count of 'banana':", fruits.count("banana"))
print("Index of 'mango':", fruits.index("mango"))

numbers = (1, 2, 3)
combined = fruits + numbers
print("Concatenated tuple:", combined)

repeated = numbers * 3
print("Repeated tuple:", repeated)