import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
for v5 in range(v1):
    if v3[v5] >= 0:
        v4 = v5
        break
v6 = 10 ** 9
if v4 + v2 - 1 < v1:
    v6 = v3[v4 + v2 - 1]
if v4 - v2 >= 0 and v6 > abs(v3[v4 - v2]):
    v6 = abs(v3[v4 - v2])
for v5 in range(1, v2):
    if v4 + v2 - v5 - 1 > v1 - 1 or v4 - v5 < 0:
        continue
    if v3[v4 + v2 - v5 - 1] + 2 * abs(v3[v4 - v5]) < v6:
        v6 = v3[v4 + v2 - v5 - 1] + 2 * abs(v3[v4 - v5])
for v5 in range(1, v2):
    if v4 - v2 + v5 < 0 or v4 + v5 - 1 > v1 - 1:
        continue
    if abs(v3[v4 - v2 + v5]) + 2 * v3[v4 + v5 - 1] < v6:
        v6 = abs(v3[v4 - v2 + v5]) + 2 * v3[v4 + v5 - 1]
print(v6)
