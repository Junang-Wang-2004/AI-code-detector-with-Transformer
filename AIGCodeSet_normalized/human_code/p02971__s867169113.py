v1 = int(input())
v2 = 0
v3 = 0
v4 = -1
for v5 in range(v1):
    v6 = int(input())
    if v2 < v6:
        v2 = v6
        v4 = v5
    elif v3 < v6:
        v3 = v6
for v5 in range(v1):
    if v5 == v4:
        print(v3)
    else:
        print(v2)
