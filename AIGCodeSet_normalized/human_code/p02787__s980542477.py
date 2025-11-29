import sys

def f1():
    return sys.stdin.buffer.readline()[:-1]
v1, v2 = map(int, f1().split())
v3 = [list(map(int, f1().split())) for v4 in range(v2)]
v5 = [10 ** 30 for v4 in range(v1 + 1)]
v5[0] = 0
for v6, v7 in v3:
    for v8 in range(v1):
        v5[min(v8 + v6, v1)] = min(v5[min(v8 + v6, v1)], v5[v8] + v7)
print(v5[v1])
