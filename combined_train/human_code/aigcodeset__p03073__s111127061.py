import sys
input = sys.stdin.readline
v1 = list(map(int, input().rstrip('\n')))
v2 = []
v3 = []
for v4 in range(len(v1)):
    if v4 % 2 == 0:
        v2.append(0)
        v3.append(1)
    else:
        v2.append(1)
        v3.append(0)
v5 = 0
v6 = 0
for v4 in range(len(v1)):
    if v2[v4] != v1[v4]:
        v5 += 1
    if v3[v4] != v1[v4]:
        v6 += 1
print(min(v5, v6))
