v1, v2 = map(int, input().split(' '))
v3 = []
for v4 in range(v1):
    v5 = list(map(int, input().split(' ')))
    v3.append(v5)
v3 = [x[0] for v6 in v3 if v6[1] <= v2]
if not v3:
    print('TLE')
else:
    print(min(v3))
