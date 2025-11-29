v1, v2 = map(int, input().split())
v3, v4, v5 = map(int, input().split())
v6 = input()
v7 = 0
v8 = []
for v9 in range(v1):
    if v9 >= v2 and v6[v9] == v8[v9 - v2]:
        v8.append(v1)
        continue
    elif v6[v9] == 'r':
        v7 += v5
        v8.append('r')
    elif v6[v9] == 's':
        v7 += v3
        v8.append('s')
    elif v6[v9] == 'p':
        v7 += v4
        v8.append('p')
print(v7)
