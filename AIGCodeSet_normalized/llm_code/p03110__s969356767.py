v1 = int(input())
v2 = {'JPY': 0, 'BTC': 0}
for v3 in range(v1):
    v4, v5 = map(str, input().split())
    v4 = float(v4)
    if v5 == 'JPY':
        v2['JPY'] = v2['JPY'] + v4
    else:
        v2['BTC'] = v2['BTC'] + v4
v6 = v2['JPY'] + v2['BTC'] * 380000.0
print(v6)
