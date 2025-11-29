v1, v2 = map(int, input().split())
v3 = []
v4 = 1
v5 = int(v1 / 0.08) + int(v2 / 0.1) + 2
for v4 in range(0, v5):
    if int(0.08 * v4) == v1 and int(0.1 * v4) == v2:
        v3.append(v4)
if len(v3) != 0:
    print(min(v3))
else:
    print(-1)
