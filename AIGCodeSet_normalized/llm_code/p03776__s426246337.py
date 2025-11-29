import sys
sys.setrecursionlimit(10 ** 9)
v1 = {0: 1, 1: 1}

def f1(a1):
    global f_memo
    if a1 in v1:
        return v1[a1]
    else:
        v1 = a1 * f1(a1 - 1)
        v1[a1] = v1
        return v1
v2 = {}

def f2(a1, a2):
    global comb_memo
    if (a1, a2) in v2:
        return v2[a1, a2]
    else:
        v1 = f1(a1)
        v2 = f1(a1 - a2)
        v3 = f1(a2)
        v4 = v1 // v2 // v3
        v2[a1, a2] = v4
        return v4
v3, v4, v5 = map(int, input().split())
v6 = list(map(int, input().split()))
v6.sort(reverse=True)
v7 = sum(v6[:v4]) / v4
v8 = v4 - 1
for v9 in range(v4, v3):
    if v6[v9] == v7:
        v8 = v9
    else:
        break
v8 += 1
v10 = 0
if v8 > v4:
    for v9 in range(v4, v5 + 1):
        v10 += f2(v8, v9)
else:
    v11 = v6[v4 - 1]
    v12 = v6.count(v11)
    v13 = v6[:v4].count(v11)
    v10 += f2(v12, v13)
print(v7)
print(v10)
