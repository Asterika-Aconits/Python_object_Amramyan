n = int(input())
control = 0
i = 2
while i < n:
    if not(n % i):
        control += 1
        break
    i += 1

if n != 2:
    if control == 1:
        print("число не простое")
    else:
        print("число простое")
else:
    print("число не простое")