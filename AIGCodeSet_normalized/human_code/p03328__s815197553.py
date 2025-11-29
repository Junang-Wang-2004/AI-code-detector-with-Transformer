v1, v2 = [int(i) for v3 in input().split()]
v4 = v2 - v1
v5 = 0
for v3 in range(1000):
    v5 += v3
    if v4 == v3:
        break
print(v5 - v2)
