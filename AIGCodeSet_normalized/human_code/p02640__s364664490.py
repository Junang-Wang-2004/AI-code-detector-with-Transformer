v1, v2 = map(int, input().split())
for v3 in range(0, v1 + 1):
    if 2 * v3 + 4 * (v1 - v3) == v2:
        print('Yes')
        exit()
print('No')
