v1 = 10 ** 9 + 7
v2 = int(input())
if v2 == 1:
    print(0)
elif v2 == 2:
    print(2)
else:
    v3 = pow(10, v2 - 2, v1) * 2 % v1
    print(v3)
