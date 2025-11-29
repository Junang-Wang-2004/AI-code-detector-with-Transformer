v1 = int(input())
v2 = list(map(int, input().split()))
if v1 == 1:
    print('Yes')
    exit()
elif v1 == 2:
    if v2[1] - v2[2] <= 1:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
for v3 in range(v1 - 2):
    if v2[v3] - v2[v3 + 1] >= 2:
        print('No')
        exit()
    elif v2[v3] - v2[v3 + 1] == 1 and v2[v3 + 1] > v2[v3 + 2]:
        print('No')
        exit()
if v2[-3] - v2[-2] == 1 and v2[-2] - v2[-1] == 1:
    print('No')
    exit()
elif v2[-2] - v2[-1] >= 2:
    print('No')
    exit()
print('Yes')
