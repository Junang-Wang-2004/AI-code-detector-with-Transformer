v1 = input()
v2 = 0
v3 = 0
for v4 in range(len(v1)):
    if v1[v4] == 'A':
        v2 = v4
        break
for v5 in range(len(v1)):
    if v1[-v5 - 1] == 'Z':
        v3 = len(v1) - 1 - v5
        break
print(v3 - v2 + 1)
