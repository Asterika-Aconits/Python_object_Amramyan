a, b, c, d = int(input()), int(input()), int(input()), int(input())
numbers = 0
if not(a % 2):
    numbers += 1

if not(b % 2):
    numbers += 1

if not(c % 2):
    numbers += 1

if not(d % 2):
    numbers += 1

print(numbers)
