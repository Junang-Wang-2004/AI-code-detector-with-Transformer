v1, v2 = map(int, input().split())
v3 = {}
v4 = []

def f1(a1):
    return str(a1).zfill(6)
for v5 in range(1, v2 + 1):
    v6, v7 = map(int, input().split())
    v8 = {'id': v5, 'ken': v6, 'year': v7}
    v4.append(v8)
v4.sort(key=lambda x: x['year'])
for v9 in range(1, v1 + 1):
    v10 = 1
    for v11 in v4:
        if v11['ken'] == v9:
            v11['shi_id'] = v10
            v10 += 1
v4.sort(key=lambda x: x['id'])
for v12 in v4:
    v13 = f1(v12['ken'])
    v14 = f1(v12['shi_id'])
    print(v13 + v14)
