def f1(a1):
    if a1 < 2:
        return 1
    else:
        return a1 * f1(a1 - 2)
v1 = int(input())
v2 = f1(v1)
v3 = 0
while v2 % 10 == 0:
    v2 //= 10
    v3 += 1
print(v3)
