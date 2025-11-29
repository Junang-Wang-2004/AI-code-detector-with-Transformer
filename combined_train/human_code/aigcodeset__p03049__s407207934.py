v1 = int(input())
v2 = 0
v3 = 0
v4 = 0
v5 = 0
for v6 in range(v1):
    v7 = input()
    v5 += v7.count('AB')
    if v7.endswith('A') and v7.startswith('B'):
        v4 += 1
    else:
        if v7.endswith('A'):
            v2 += 1
        if v7.startswith('B'):
            v3 += 1
if v4 == 0:
    v5 += min(v2, v3)
else:
    v5 += v4 - 1
    if v2 > 0:
        v2 -= 1
        v5 += 1
    if v3 > 0:
        v3 -= 1
        v5 += 1
    v5 += min(v2, v3)
print(v5)
