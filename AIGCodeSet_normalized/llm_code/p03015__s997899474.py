import sys
v1 = lambda: sys.stdin.readline().rstrip()
v2 = lambda: int(v1())
v3 = lambda: list(map(int, v1().split()))
v4 = 10 ** 9 + 7
v5 = v1()
v6 = (1, 2)
v7 = len(v5)
for v8 in range(1, v7):
    v9 = v6[:]
    if v5[v8] == '1':
        v6[0] = v9[0] * 3 + v9[1]
        v6[1] = v9[1] * 2
    else:
        v6[0] = v9[0] * 3
        v6[1] = v9[1]
v10 = sum(v6)
print(v10 % v4)
