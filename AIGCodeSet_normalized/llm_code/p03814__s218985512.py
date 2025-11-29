v1 = list(input())
v2 = [i for v3, v4 in enumerate(v1) if v4 == 'A']
v5 = [v3 for v3, v4 in enumerate(v1) if v4 == 'Z']
v6 = []
for v3 in v2:
    for v7 in v5:
        if v3 < v7:
            v8 = v7 - v3 + 1
            v6.append(v8)
        else:
            break
print(max(v6))
