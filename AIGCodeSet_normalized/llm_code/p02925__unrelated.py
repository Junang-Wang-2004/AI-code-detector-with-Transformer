def f1(a1, a2):
    for v1 in range(a1):
        for v2 in range(a1 - 1):
            if a2[v1][v2] == v1 or a2[v1][v2] < 1 or a2[v1][v2] > a1:
                return False
        if len(set(a2[v1])) != a1 - 1:
            return False
    return True

def f2(a1, a2):
    if not f1(a1, a2):
        return -1
    v1 = [[] for v2 in range(a1)]
    for v3 in range(a1):
        for v4 in range(a1 - 1):
            v1[v3].append(a2[v3][v4])
    v5 = 0
    v6 = [[] for v2 in range(a1)]
    for v3 in range(a1):
        for v4 in range(a1 - 1):
            for v7 in range(a1):
                if v3 not in v6[v7] and a2[v3][v4] not in v6[v7]:
                    v6[v7].append(v3)
                    v6[v7].append(a2[v3][v4])
                    break
            else:
                v5 += 1
                v6.append([v3, a2[v3][v4]])
    return v5
v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(list(map(int, input().split())))
v4 = f2(v1, v2)
print(v4)
