v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = [int(s) for v5 in v2]
v6 = sorted(v4)
v7 = sum(v4)
v8 = 0
if v7 % 10 != 0:
    print(v7)
else:
    while v8 < v1 and v6[v8] % 10 == 0:
        v8 += 1
    if v8 == v1:
        print(0)
    else:
        print(v7 - v6[v8])
