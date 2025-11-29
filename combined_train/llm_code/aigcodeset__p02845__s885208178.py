v1: N = int(input())
v2 = list(map(int, input().split()))
v3 = {'R': 0, 'G': 0, 'B': 0}
v4 = 1
v5 = True
for v6 in range(N):
    if v2[v6] == v3['R']:
        v3['R'] += 1
        v7 = v3['R'] == v3['G'] == v3['B'] + 1
        v4 *= v7
    elif v2[v6] == v3['G']:
        v3['G'] += 1
        v7 = v3['G'] == v3['B'] + 1
        v4 *= v7
    elif v2[v6] == v3['B']:
        v3['B'] += 1
        v7 = v3['R'] == v3['G'] == v3['B'] + 1
        v4 *= v7
    else:
        v5 = False
        break
if v5:
    print(v4 % 1000000007)
else:
    print(0)
