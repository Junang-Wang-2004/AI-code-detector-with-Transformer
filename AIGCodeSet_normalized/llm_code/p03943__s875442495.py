v1 = list(map(int, input().split()))
v1.sort()
if v1[0] + v1[1] == v1[2]:
    print('Yes')
else:
    print('No')
