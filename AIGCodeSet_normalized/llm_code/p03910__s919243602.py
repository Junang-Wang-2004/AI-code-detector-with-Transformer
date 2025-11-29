v1 = int(input())
v2 = 0
v3 = []
for v4 in range(1, v1 + 1):
    v3.append(v4)
    v2 += v4
    if v2 == v1:
        break
    elif v1 - v2 < v4:
        v2 -= v4
        v3.pop()
for v4 in v3:
    print(v4)
