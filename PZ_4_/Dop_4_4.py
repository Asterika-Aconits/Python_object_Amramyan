n = int(input())
i = 1
summ = 0

while i <= n:
    temp_summ = 1
    temp_i = 1
    while temp_i <= i:
        temp_summ *= temp_i
        temp_i += 1
    print(f"факториал {i} = {temp_summ}")
    summ += temp_summ
    i += 1

print("сумма: ", summ)