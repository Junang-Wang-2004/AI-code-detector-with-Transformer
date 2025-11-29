v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = list(reversed(sorted(v2)))
v5 = v4[0]
v6 = v2.count(v5) >= 2
if v6:
    v7 = (str(v5) + '\n') * v1
    print(v7)
    exit()
v8 = None
for v9 in v4:
    if v9 < v5:
        v8 = v9
        break
v7 = [v8 if v9 == v5 else v5 for v9 in v2]
v7 = '\n'.join(map(str, v7))
print(v7)
