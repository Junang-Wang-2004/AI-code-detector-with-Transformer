import sys
v1 = int(input())
v2 = sorted(list(map(int, input().split())))
v3 = v2[0]
v4 = v2[-1]
if v1 == 2:
    print(v2[1] - v2[0])
    print(v2[1], v2[0])
    sys.exit()
v5 = []
for v6 in v2[1:-1]:
    if v6 <= 0:
        v5.append([v4, v6])
        v4 -= v6
    else:
        v5.append([v3, v6])
        v3 -= v6
v5.append([v4, v3])
print(v4 - v3)
for v7 in v5:
    print(v7[0], v7[1])
