v1 = int(input())
v2 = int(input())
v3 = 0
for v4 in range(v1 - 1):
    v5 = int(input())
    if v5 == v2:
        continue
    elif v5 > v2:
        v3 += v5 - v2
        v2 = v5
    else:
        v3 = -1
        break
print(v3)
