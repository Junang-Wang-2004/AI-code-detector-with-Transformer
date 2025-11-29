v1 = input()
v2 = len(v1)
v3 = [1] * v2
for v4 in range(v2 - 2):
    if v1[v4:v4 + 2] == 'RR':
        v3[v4 + 2] += v3[v4]
        v3[v4] = 0
for v4 in reversed(range(1, len(v3) - 1)):
    if v1[v4 - 1:v4 + 1] == 'LL':
        v3[v4 - 2] += v3[v4]
        v3[v4] = 0
print(' '.join(map(str, v3)))
