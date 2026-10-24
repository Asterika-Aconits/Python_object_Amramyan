i = int(input())
start = 0
if i < 0:
    start = 30
    while start >= 10:
        print(start)
        start += i
else:
    start = 10
    while start <= 30:
        print(start)
        start += i
