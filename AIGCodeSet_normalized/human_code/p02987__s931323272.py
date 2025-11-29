v1 = 4
v2 = list(input())
v2.sort()
if v2.count(v2[0]) == 2 and v2.count(v2[v1 - 1]) == 2:
    print('Yes')
else:
    print('No')
