v1, v2 = map(int, input().split())
v3 = 1001
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    if v6 <= v2 and v5 < v3:
        v3 = v5
if v3 == 1001:
    print('TLE')
else:
    print(v3)
