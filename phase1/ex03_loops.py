numbers = [3, 7, 2, 9, 1, 5, 8, 4, 6]

max = 0
calculation = sum(numbers)

print(calculation)

for n in numbers:
  if n > max:
    max = n

print(max)