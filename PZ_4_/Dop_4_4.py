n = int(input())
i = 1

print("S=", end="")
while i <= n:
    if i == 1:
        print(f"{i}!", end="")
        i += 1
        continue

    print(f"+{i}!", end="")
    i += 1
