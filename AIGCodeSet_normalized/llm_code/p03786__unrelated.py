import sys
v1 = int(sys.stdin.readline())
v2 = list(map(int, sys.stdin.readline().split()))
v3 = set(range(1, v1 + 1))
for v4 in range(v1):
    for v5 in range(v4 + 1, v1):
        if v2[v4] <= 2 * v2[v5]:
            v3.remove(v4 + 1)
            break
        elif v2[v5] <= 2 * v2[v4]:
            v3.remove(v5 + 1)
            break
print(len(v3))
