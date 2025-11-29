v1, v2 = map(int, input().split())
v3 = []
v4 = []
v5 = float('inf')
for v6 in range(v1):
    v7 = input().split()
    v3.append(int(v7[0]))
    v4.append(int(v7[1]))
for v8 in range(v1):
    if v4[v8] <= v2:
        v5 = min(v5, v3[v8])
if v5 == float('inf'):
    print('TLE')
else:
    print(v5)
