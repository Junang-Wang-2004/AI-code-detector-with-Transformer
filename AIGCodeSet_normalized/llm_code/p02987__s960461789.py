v1 = input()
v2 = list(v1)
v3 = 0
v4 = 0
while v3 <= len(v2) - 3:
    if v2[v3 + 1] > v2[v3] and v2[v3 + 1] < v2[v3 + 2] or (v2[v3 + 1] < v2[v3] and v2[v3 + 1] > v2[v3 + 2]):
        v4 += 1
        v3 += 1
    else:
        v3 += 1
if len(set(v2)) == 2 and v4 == 1:
    print('Yes')
else:
    print('No')
