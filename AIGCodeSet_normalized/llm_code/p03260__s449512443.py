v1 = 1
v2, v3 = map(int, input().split())
v4 = {}
while v1 < 3:
    v4[v1] = v2 * v3 * v1 % 2
    v1 = v1 + 1
v1 = 1
v5 = 'No'
while v1 < 3:
    if v4[v1] == 1:
        v5 = 'Yes'
        break
    v1 = v1 + 1
print(v5)
