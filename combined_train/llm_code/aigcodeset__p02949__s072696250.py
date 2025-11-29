import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v2):
    v6, v7, v8 = map(int, input().split())
    v4.append([v6 - 1, v7 - 1, -v8 + v3])

def f1(a1, a2, a3):
    v1 = float('inf')
    v2 = [v1 for v3 in range(a3)]
    v2[a2] = 0
    for v3 in range(2 * a3):
        for v4, v5, v6 in a1:
            if v4 != v1 and v2[v5] > v2[v4] + v6:
                v2[v5] = v2[v4] + v6
        if v3 == a3 - 2:
            v7 = v2[-1]
    return (v7, v2[-1])
v9, v10 = f1(v4, 0, v1)
if v9 != v10:
    v11 = -1
else:
    v11 = max(0, -v10)
print(v11)
