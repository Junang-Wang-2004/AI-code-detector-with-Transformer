v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v2.sort()
v4 = [v2[0], v2[-1]]
v5 = abs(v2[0] - v2[-1])
v6 = 1
v7 = v1 - 2
if v1 == 2:
    print(v5)
    exit()
while True:
    v8 = 0
    v9 = 's'
    v10 = 's'
    if v8 < abs(v4[0] - v2[v6]):
        v8 = abs(v4[0] - v2[v6])
        v9 = 's'
        v10 = 's'
    if v8 < abs(v4[0] - v2[v7]):
        v8 = abs(v4[0] - v2[v7])
        v9 = 'e'
        v10 = 's'
    if v8 < abs(v4[1] - v2[v6]):
        v8 = abs(v4[1] - v2[v6])
        v9 = 's'
        v10 = 'e'
    if v8 < abs(v4[1] - v2[v7]):
        v8 = abs(v4[1] - v2[v7])
        v9 = 'e'
        v10 = 'e'
    v5 += v8
    if v10 == 's':
        if v9 == 's':
            v4[0] = v2[v6]
        if v9 == 'e':
            v4[0] = v2[v7]
    if v10 == 'e':
        if v9 == 's':
            v4[1] = v2[v6]
        if v9 == 'e':
            v4[1] = v2[v7]
    if v9 == 's':
        v6 += 1
    if v9 == 'e':
        v7 -= 1
    if v6 - 1 == v7:
        break
print(v5)
