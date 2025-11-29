import sys
input = sys.stdin.readline
v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = 0
for v5 in range(1, v1 - 1):
    for v6 in range(v5 + 1, v1):
        for v7 in range(v6 + 1, v1 + 1):
            if v2[v5 - 1] != v2[v6 - 1] and v2[v6 - 1] != v2[v7 - 1] and (v2[v7 - 1] != v2[v5 - 1]) and (v6 - v5 != v7 - v6):
                v4 += 1
print(v4)
