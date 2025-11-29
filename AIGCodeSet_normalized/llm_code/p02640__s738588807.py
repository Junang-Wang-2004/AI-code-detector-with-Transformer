v1, v2 = map(int, input().split())
v3 = 'No'
for v4 in range(v1 + 1):
    v5 = v1 - v4
    if v4 * 2 + v5 * 4 == v2:
        v3 = 'Yes'
        break
print(v3)
