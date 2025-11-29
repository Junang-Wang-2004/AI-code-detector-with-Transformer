from sys import stdin
v1 = int(stdin.readline())
v2 = [0] * 3
for v3 in range(v1):
    v4 = [0, 0, 0]
    v5 = list(map(int, stdin.readline().split()))
    for v3 in range(3):
        v4[v3] = max(v2[(v3 + 1) % 3], v2[(v3 + 2) % 3]) + v5[v3]
    v2 = v4
print(max(v2))
