v1 = int(input())
v2 = input()
v3 = v2.count('#')
v4 = v1 - v3
v5 = 0
v6 = 0
for v7 in range(v1):
    if v2[v7] == '#':
        v5 = v7
        break
for v7 in range(v1):
    if v2[~v7] == '.':
        v6 = ~v7 + v1
        break
v8 = min(v3 - v5, v4 - v6)
print(v8)
