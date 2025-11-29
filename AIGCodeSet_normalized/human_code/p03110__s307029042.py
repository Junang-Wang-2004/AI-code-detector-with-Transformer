v1 = int(input().strip())
v2 = []
for v3 in range(v1):
    v2.append(list(map(str, input().strip().split(' '))))
v4 = 0
for v3 in range(v1):
    if v2[v3][1] == 'BTC':
        v4 = v4 + float(v2[v3][0]) * 380000
    else:
        v4 = v4 + float(v2[v3][0])
print(v4)
