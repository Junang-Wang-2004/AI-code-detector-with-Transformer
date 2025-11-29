v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = list(map(int, input().split()))
    v2 += [v4]
v2.sort(reverse=False)
v5 = []
for v3 in range(v1):
    v4 = list(map(int, input().split()))
    v5 += [v4]
v5.sort(reverse=False)

def f1(a1):
    v1 = 10 ** 9
    v2 = 0
    v3 = -1
    for v4 in range(v1):
        if v5[a1][0] > v2[v4][0]:
            if v3 < v2[v4][1] and v5[a1][1] > v2[v4][1]:
                v2 = 1
                v3 = max(v3, v2[v4][1])
                v5 = v4
    if v2 == 0:
        return False
    else:
        v2[v5][0] = v1
        v2[v5][1] = v1
        return True
v6 = 0
for v7 in range(v1):
    if f1(v7):
        v6 += 1
print(v6)
