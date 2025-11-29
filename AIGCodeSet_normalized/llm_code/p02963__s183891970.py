v1 = int(input())
v2 = 0
v3 = 0
if v1 > 10 ** 9:
    v4 = 10 ** 9
    v5 = 1
    v6 = v1 // v4
    v7 = v1 % v4
else:
    v4 = v1
    v5 = 0
    v6 = 0
    v7 = 1
print(v2, v3, v4, v5, v6, v7)
