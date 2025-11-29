v1 = int(input())
v2 = list(map(int, input().split()))
v3 = {}
for v4 in range(v1):
    if v2[v4] not in v3.keys():
        v3[v2[v4]] = 0
    else:
        v3[v2[v4]] += 1
v5 = []
for v6 in v3.values():
    v5.append(v6)
v7 = sorted(v5, reverse=True)
if v7[0] - v7[1] >= sum(v7[1:]):
    print(v1 - v7[0] * 2)
elif sum(v7[0:]) % 2 == 0:
    print(len(v7))
else:
    print(len(v7) - 1)
