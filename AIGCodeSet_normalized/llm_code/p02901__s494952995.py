v1, v2 = input().split()
v1, v2 = (int(v1), int(v2))
v3 = [0 for v4 in range(v2)]
v5 = [[] for v4 in range(v2)]
for v6 in range(v2):
    v3[v6], v7 = input().split()
    v3[v6], v7 = (int(v3[v6]), int(v7))
    v5[v6] = list(map(int, input().split()))
    v5[v6] = [j - 1 for v8 in v5[v6]]

def f1(a1, a2):
    if a1 == v1 and 0 not in a2:
        return 0
    elif a1 == v1 and 0 in a2:
        return 1e+20
    else:
        v1 = f1(a1 + 1, a2)
        v2 = a2.copy()
        for v3 in range(len(v5[a1])):
            v2[v5[a1][v3]] += 1
        v4 = f1(a1 + 1, v2) + v3[a1]
        return min([v1, v4])
v9 = [0 for v4 in range(v1)]
v10 = f1(0, v9)
if v10 >= 1e+20:
    print(-1)
else:
    print(v10)
