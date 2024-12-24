# Your code below:
single_digits = list(range(10))
# print(single_digits)
squares = []

for digit in single_digits:
  squares.append(digit**2)
  print(digit)
print(squares)

cubes = [digit**3 for digit in single_digits]

print(cubes)


