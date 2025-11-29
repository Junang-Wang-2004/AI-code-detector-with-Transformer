v1 = input()
v2 = input()
v3 = len(v2)
v4 = ''
if len(v1) - len(v2) == 0:
    for v5 in range(v3):
        v4 = v4 + v1[v5] + v2[v5]
    print(v4)
else:
    for v5 in range(v3):
        v4 = v4 + v1[v5] + v2[v5]
    v4 = v4 + v1[v3]
    print(v4)
