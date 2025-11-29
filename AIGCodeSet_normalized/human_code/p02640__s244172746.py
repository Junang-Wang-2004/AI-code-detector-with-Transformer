v1, v2 = [int(v) for v3 in input().split()]
v4 = 'No'
for v5 in range(v1 + 1):
    v6 = v1 - v5
    if 2 * v5 + 4 * v6 == v2:
        v4 = 'Yes'
        break
print(v4)
