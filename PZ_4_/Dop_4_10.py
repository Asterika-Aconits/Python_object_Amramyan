n = int(input())
number = 0
fibo_a = 0
fibo_b = 1
while fibo_a <= n and fibo_b:
    if not(fibo_a % 2):
        number += 1
    if not (fibo_b % 2):
        number += 1
    print(fibo_a, fibo_b)
    fibo_a = fibo_a + fibo_b
    fibo_b = fibo_a + fibo_b

print("число четных:", number)
