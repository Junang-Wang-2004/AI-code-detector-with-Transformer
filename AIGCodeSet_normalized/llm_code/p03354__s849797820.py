v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = []
for v5 in range(0, v2):
    v4.append(list(map(int, input().split())))
v6 = set(range(1, v1 + 1))
v7 = 0
while v6:
    v8 = {v6.pop()}
    for v9 in range(0, 2):
        for v5 in v4:
            if v8 & set(v5):
                v8 = v8 | set(v5)
                v4.remove(v5)
    for v5 in list(v8):
        if v3[v5 - 1] in v8:
            v7 += 1
    v6 = v6 - (v6 & v8)
print(v7)
