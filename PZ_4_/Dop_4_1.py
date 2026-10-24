n = 4
i = 1
negativ = 0
summ = 0
while i <= n:
    number = int(input())
    summ += number
    if number < 0:
        negativ += 1
    i += 1

print(f"колличество отрицательных: {negativ}")
print(f"Сумма: {summ}")
