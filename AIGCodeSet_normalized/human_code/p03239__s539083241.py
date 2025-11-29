v1, v2 = map(int, input().split())
v3 = False
v4 = float('inf')
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    if v7 <= v2 and v6 < v4:
        v4 = v6
        v3 = True
print(v4 if v3 else 'TLE')
