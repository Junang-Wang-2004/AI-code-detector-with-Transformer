v1, v2 = map(int, input().split())
for v3 in range(v1 + 1):
    v4 = v3
    v5 = v1 - v4
    if v4 * 2 + v5 * 4 == v2:
        print('Yes')
        break
else:
    print('No')
