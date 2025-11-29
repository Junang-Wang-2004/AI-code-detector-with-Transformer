v1 = int(input())
v2 = 0
v3, v4, v5 = (0, 0, 0)
for v6 in range(v1):
    v7 = input()
    v2 += v7.count('AB')
    if v7[-1] == 'A':
        v3 += 1
    if v7[0] == 'B':
        v4 += 1
    if v7[0] == 'B' and v7[-1] == 'A':
        v5 += 1
print(v2 + min(v3, v4) + (v5 - min(v3, v4)))
