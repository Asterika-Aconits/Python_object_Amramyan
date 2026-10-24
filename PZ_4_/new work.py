n = int(input("Введите границы степени:"))
i = 1
while True:
    if 2**i < n:
        print(2**i)
        i += 1
    else:
        break