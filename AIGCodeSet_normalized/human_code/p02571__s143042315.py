v1 = input()
v2 = input()
v3 = len(v2)
if v2 in v1:
    print(0)
    exit(0)
v4 = v3
for v5 in range(len(v1) - v3 + 1):
    v6 = v1[v5:v5 + v3]
    v7 = v3
    for v8 in range(v3):
        if v6[v8] == v2[v8]:
            v7 = v7 - 1
    if v7 < v4:
        v4 = v7
print(v4)
