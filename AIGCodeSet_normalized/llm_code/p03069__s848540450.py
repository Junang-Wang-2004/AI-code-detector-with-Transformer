v1 = input()
v2 = input()
v3 = 0
v4 = 0
v5 = list()
for v6 in v2:
    v5.append(v6)
if '#' in v5:
    v7 = v5.index('#')
    v8 = v5.count('.')
    v9 = v8 - v7
    v10 = v5.count('#')
    v4 = v9
    if v10 < v9:
        v4 = v10
else:
    v4 = 0
print(v4)
