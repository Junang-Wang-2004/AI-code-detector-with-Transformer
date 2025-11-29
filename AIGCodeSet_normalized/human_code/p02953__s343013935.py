v1 = int(input())
v2 = list(map(int, input().split()))[::-1]
v3 = 10 ** 10
for v4 in v2:
    if v3 >= v4:
        v3 = v4
    elif v3 == v4 - 1:
        v3 = v4 - 1
    else:
        print('No')
        exit(0)
print('Yes')
