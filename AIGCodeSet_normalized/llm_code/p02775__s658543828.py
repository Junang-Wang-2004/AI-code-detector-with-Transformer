v1 = int(input())
v2 = 0
v3 = 0
while v1 > 0:
    if v1 % 10 >= 5:
        v3 += 10 - v1 % 10
        v1 += 1
    else:
        v3 += v1 % 10
    v1 //= 10
print(v3)
