n = int(input())
i = 1
zero = 0
while i <= n:
    number = int(input())
    if number == 0:
        zero += 1

print("колличество нулей:", zero)
