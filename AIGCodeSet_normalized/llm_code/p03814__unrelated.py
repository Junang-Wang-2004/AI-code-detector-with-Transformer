v1 = input()
v2 = len(v1)
v3 = 0
v4 = 0
for v5 in range(v2):
    if v1[v5] == 'A':
        v3 = v5
    if v1[v5] == 'Z':
        v4 = v5
print(v4 - v3 + 1)
