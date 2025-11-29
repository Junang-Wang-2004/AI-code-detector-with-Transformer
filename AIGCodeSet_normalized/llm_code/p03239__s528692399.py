v1, v2 = [int(s) for v3 in input().split()]
v4 = 10000
for v5 in range(v1):
    v6, v7 = [int(v3) for v3 in input().split()]
    if v7 <= v2:
        v4 = min(v4, v6)
if v4 == 10000:
    print('TLE')
else:
    print(v4)
