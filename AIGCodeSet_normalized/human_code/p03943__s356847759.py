v1 = 3
v2 = [0] * v1
v2[:] = map(int, input().split())
v2.sort()
if sum(v2) == 2 * v2[v1 - 1]:
    print('Yes')
else:
    print('No')
