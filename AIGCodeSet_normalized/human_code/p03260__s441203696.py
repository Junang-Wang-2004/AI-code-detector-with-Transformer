v1, v2 = map(int, input().split())
for v3 in range(1, 4):
    if v1 * v2 * v3 % 2 != 0:
        print('Yes')
        break
    else:
        print('No')
        break
