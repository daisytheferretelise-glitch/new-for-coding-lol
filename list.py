numbers = [1, 2, 3, 4, 5]

squares = [n * 2 for n in numbers]
print("Squares:", squares)

evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

square_evens = [n * n for n in numbers if n % 2 == 0]
print("Squares of even numbers:", square_evens)

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print("Pairs:", pairs)
