print("Bob was sleepy in class and the teacher wanted him to make a cube base a exponent and his results")

base = 2
exponent = 5
result = 1

for _ in range(exponent):
    result *= base

print(result)  # Output: 32

if result != 1:
    print("Bob got it right but was still scolded")
else:
    print("Bob got it wrong and got a detention")
