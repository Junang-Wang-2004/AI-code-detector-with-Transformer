v1, v2 = map(int, input().split())
v3 = {}
for v4 in range(v2):
    v5, v6 = input().split()
    v5 = int(v5)
    if v5 not in v3:
        v3[v5] = {'ac': False, 'wa': 0}
    if v6 == 'AC' and (not v3[v5]['ac']):
        v3[v5]['ac'] = True
    elif v6 == 'WA' and (not v3[v5]['ac']):
        v3[v5]['wa'] += 1
v7 = len(v3)
v8 = sum((v3[v5]['wa'] for v5 in v3))
print(v7, v8)
