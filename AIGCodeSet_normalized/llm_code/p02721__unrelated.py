v1, v2, v3 = map(int, input().split())
v4 = input()
v5 = []
for v6 in range(v1):
    if v4[v6] == 'x':
        continue
    if len(v5) == 0:
        v5.append(v6 + 1)
    elif v5[-1] + v3 + 1 <= v6 + 1:
        v5.append(v6 + 1)
if len(v5) == v2:
    for v7 in v5:
        print(v7)
else:
    print(-1)
