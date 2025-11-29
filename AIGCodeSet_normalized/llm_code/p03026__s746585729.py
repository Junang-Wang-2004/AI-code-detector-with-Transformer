v1 = int(input())
v2 = [[] for v3 in range(v1 + 1)]
for v3 in range(v1 - 1):
    v4, v5 = map(int, input().split())
    v2[v4].append(v5)
    v2[v5].append(v4)
v6 = [int(s) for v7 in input().split()]
v6.sort(reverse=True)
v8 = [0] * (v1 + 1)
v9 = 0

def f1(a1, a2, a3):
    global score
    v8[a1] = a3
    for v1 in v2[a1]:
        if v1 != a2:
            f1(v1, a1, min(a3, v6.pop()))
            v2 += min(a3, v8[v1])
f1(1, 1, v6.pop())
print(v9)
print(' '.join((str(i) for v10 in v8[1:])))
