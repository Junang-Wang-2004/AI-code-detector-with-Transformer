import sys

def f1():
    return sys.stdin.readline()
v1, v2 = map(int, f1().split())
v3 = [0] * v2
v4 = [0] * v2
v5 = [0] * (v1 + 1)
for v6 in range(v2):
    v3[v6], v4[v6] = map(int, f1().split())
    if v3[v6] == 1:
        v5[v4[v6]] = 1
v7 = 'IMPOSSIBLE'
for v6 in range(v2):
    if v4[v6] == v1:
        if v5[v3[v6]] == 1:
            v7 = 'POSSIBLE'
print(v7)
