import sys

def f1():
    return sys.stdin.readline().strip()

def f2():
    return map(int, f1().split())
sys.setrecursionlimit(10 ** 9)
v1, v2 = f2()
v3 = [1] * 50
v4 = [1] * 50
for v5 in range(1, 50):
    v3[v5] = v3[v5 - 1] * 2 + 3
    v4[v5] = v4[v5 - 1] * 2 + 1
v6 = v2
v7 = v1
v8 = 0
while 1:
    if v6 <= 1:
        break
    if v7 == 0:
        break
    elif v6 == v3[v7 - 1] + 2:
        v8 += v4[v7 - 1] + 1
        break
    elif v6 == v3[v7 - 1] + 1:
        v8 += v4[v7 - 1]
        break
    elif v6 <= v3[v7 - 1]:
        v7 -= 1
        v6 -= 1
        continue
    else:
        v8 += v4[v7 - 1] + 1
        v6 -= v3[v7 - 1] + 2
        v7 -= 1
if v6 == 1:
    v8 += 1
print(v8)
