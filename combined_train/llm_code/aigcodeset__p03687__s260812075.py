import math
v1 = input().rstrip()
v2 = set()
for v3 in range(len(v1)):
    v2.add(v1[v3])
if len(v2) == len(v1):
    print(math.ceil(len(v1) // 2))
elif len(v2) == 1:
    print(0)
else:
    v4 = 1
    for v5 in range(1, len(v1) - 1):
        if v4 < v1.count(v1[v5]):
            v4 = v1.count(v1[v5])
    v6 = set()
    for v7 in range(1, len(v1) - 1):
        if v1.count(v1[v7]) == v4:
            v6.add(v1[v7])
    v8 = 10 ** 12
    for v9 in v6:
        v10 = list(v1)
        v11 = 0
        while len(set(v10)) > 1:
            v11 += 1
            v12 = []
            for v13 in range(len(v10) - 1):
                if v10[v13] == v9 or v10[v13 + 1] == v9:
                    v12.append(v9)
                else:
                    v12.append(v10[v13])
            v10 = v12
        v8 = min(v11, v8)
    print(v8)
