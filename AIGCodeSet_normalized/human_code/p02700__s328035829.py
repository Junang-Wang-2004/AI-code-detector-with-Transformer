v1, v2, v3, v4 = map(int, input().split())
v5 = v1 // v4
if v1 % v4 != 0:
    v5 += 1
v6 = v3 // v2
if v3 % v2 != 0:
    v6 += 1
if v5 < v6:
    print('No')
else:
    print('Yes')
