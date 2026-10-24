a, b, c, d = int(input()), int(input()), int(input()), int(input())
negativ = 0
if a < 0:
    negativ += 1

if b < 0:
    negativ += 1

if c < 0:
    negativ += 1

if d < 0:
    negativ += 1

print(f"колличество отрицательных: {negativ}")
print(f"Сумма: {a + b + c + d}")
