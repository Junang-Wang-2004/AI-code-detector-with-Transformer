v1 = input()
v2 = ''
for v3 in range(1, len(v1) + 1):
    v2 += v1[-v3]
if v1 == v2:
    print('Yes')
else:
    print('No')
