v1, v2 = map(int, input().split())
v3 = 10000
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    if v2 >= v6:
        v3 = min(v3, v5)
if v3 == 10000:
    print('TLE')
else:
    print(v3)
