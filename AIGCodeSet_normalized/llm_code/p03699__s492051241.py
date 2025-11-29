v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v2.sort()
v4 = sum(v2)
if v4 % 10 != 0:
    print(v4)
else:
    for v3 in range(v1 - 1, -1, -1):
        if v2[v3] % 10 != 0:
            v5 = v4 - v2[v3]
            print(v5)
            break
    if v5 == v4:
        print(0)
