v1 = int(input())
v2 = list(map(int, input().split()))
v3 = max(v2)
v4 = max(v2)
v5 = max(v2)
for v6 in v2:
    if v6 == v3:
        pass
    elif abs(v6 - v3 / 2) <= v4:
        v4 = abs(v6 - v3 / 2)
        v5 = v6
print('{} {}'.format(v3, v5))
