def f1(a1=int):
    return map(a1, input().split())
v1, v2 = f1()
v3, v4, v5 = f1()
v6, = f1(str)
v7 = []
v8 = 'rps'
for v9 in range(v1):
    if v6[v9] == 'r':
        v7.append('p')
    elif v6[v9] == 's':
        v7.append('r')
    elif v6[v9] == 'p':
        v7.append('s')
for v9 in range(v2, v1):
    if v7[v9] == v7[v9 - v2]:
        v7[v9] = '0'
v10 = 0
for v9 in range(v1):
    if v7[v9] == 'p':
        v10 += v5
    elif v7[v9] == 'r':
        v10 += v3
    elif v7[v9] == 's':
        v10 += v4
print(v10)
