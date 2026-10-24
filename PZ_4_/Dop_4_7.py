while True:
    a = int(input())
    b = int(input())
    if a < b:
        break
    print("Вы ввели не подходящее значение, а должно быть меньше б")

while a <= b:
    print(b)
    b -= 1
    