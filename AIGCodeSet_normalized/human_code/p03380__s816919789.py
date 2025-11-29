v1 = int(input())
v2 = list(map(int, input().split()))
if v1 == 2:
    print(' '.join(map(str, [max(v2), min(v2)])))
    exit()
v3 = max(v2)
v4 = v3
for v5 in v2:
    if v5 == v3:
        continue
    if abs(v5 - v3 / 2) < abs(v4 - v3 / 2):
        v4 = v5
print(' '.join(map(str, [v3, v4])))
