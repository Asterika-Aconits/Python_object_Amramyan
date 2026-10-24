while True:
    a = int(input())
    b = int(input())
    if a < b:
        break
    print("Вы ввели не подходящее значение, а должно быть меньше б")

summ = 0
while a <= b:
    summ += a
    a += 1

print(summ)
