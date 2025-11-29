v1, v2 = map(int, input().split())
if v2 % 2 == 0 and 2 * v1 <= v2 <= 4 * v1:
    print('Yes')
else:
    print('No')
