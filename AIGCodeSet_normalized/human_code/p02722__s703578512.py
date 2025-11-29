import sys
sys.setrecursionlimit(10 ** 7)
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readlines
v4 = int(input())

def f1(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 ** 2 == a1:
                continue
            v1.append(a1 // v2)
    return v1
v5 = f1(v4)
v6 = f1(v4 - 1)
v7 = []
for v8 in v5:
    if v8 == 1:
        continue
    v9 = v4
    while v9 % v8 == 0:
        v9 //= v8
    if v9 % v8 == 1 or v9 == 1:
        v7.append(v8)
for v8 in v6:
    if v8 == 1:
        continue
    if v4 % v8 == 0:
        v10 = v4 // v8
        if v10 % v8 == 1 or v10 % v8 == 0:
            v7.append(v8)
    else:
        v7.append(v8)
v7 = list(set(v7))
print(len(v7))
