v1 = int(input())
v2 = list(map(int, input().split()))
v3 = set(v2)
if len(v3) == 1:
    print(len(v2))
    exit()
v4 = v2[0]
v5 = True
for v6 in range(1, len(v2)):
    if v4 * 2 >= v2[v6]:
        v4 += v2[v6]
    else:
        v5 = False
        break
if v5:
    print(len(v2))
    exit()
v2 = sorted(v2)
v7 = 0
v8 = len(v2) - 1
v9 = (v7 + v8) // 2
while True:
    v10 = v9
    v11 = sum(v2[0:v9 + 1])
    v12 = True
    for v6 in range(v9 + 1, len(v2)):
        if v11 * 2 >= v2[v6]:
            v11 += v2[v6]
        else:
            v12 = False
            break
    if v12:
        v8 = v9
        v9 = (v7 + v8) // 2
    else:
        v7 = v9
        v9 = (v7 + v8) // 2
    if v9 == v10:
        break
print(len(v2) - len(v2[0:v9 + 1]))
