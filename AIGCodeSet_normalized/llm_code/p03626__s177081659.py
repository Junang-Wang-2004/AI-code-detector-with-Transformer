v1 = int(input())
v2 = list(input())
v3 = list(input())
v4 = 1
v5 = 0
v6 = 0
v7 = 1000000007
while v5 < v1:
    if v2[v5] == v3[v5]:
        v5 += 1
        v4 *= 3
        v4 %= v7
        v6 = 1
    else:
        v5 += 2
        v4 *= 6
        v4 %= v7
        v6 = 2
print(v4 % v7)
