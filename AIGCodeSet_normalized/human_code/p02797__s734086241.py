import sys
v1 = lambda: int(sys.stdin.readline())
v2 = lambda: map(int, sys.stdin.readline().split())
v3 = lambda: list(v2())
v4 = lambda: map(str, sys.stdin.readline().split())
v5 = lambda: list(v4())
v6, v7, v8 = v2()
v9 = [str(v8)] * v7
if v8 != 10 ** 9:
    for v10 in range(v6 - v7):
        v9.append(str(v8 + 1))
else:
    for v10 in range(v6 - v7):
        v9.append(str(v8 - 1))
print(' '.join(v9))
