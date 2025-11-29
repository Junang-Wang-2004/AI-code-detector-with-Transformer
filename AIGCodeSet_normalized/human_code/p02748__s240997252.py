import sys

def f1():
    return sys.stdin.readline()[:-1]
v1, v2, v3 = map(int, f1().split())
v4 = list(map(int, f1().split()))
v5 = list(map(int, f1().split()))
v6 = min(v4) + min(v5)
for v7 in range(v3):
    v8, v9, v10 = map(int, f1().split())
    v11 = v4[v8 - 1] + v5[v9 - 1] - v10
    if v6 > v11:
        v6 = v11
print(v6)
