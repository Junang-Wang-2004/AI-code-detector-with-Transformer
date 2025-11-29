import sys
input = sys.stdin.readline
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = max(v2)
v4 = min(v2)
v2.pop(v3)
v2.pop(v4)
v5 = v3 - v4
for v6 in range(v1 - 2):
    v5 += abs(v2[v6])
print(v5)
for v6 in range(v1 - 2):
    if v2[v6] > 0:
        print(v4, v2[v6])
        v4 -= v2[v6]
    else:
        print(v3, v2[v6])
        v3 -= v2[v6]
print(v3, v4)
