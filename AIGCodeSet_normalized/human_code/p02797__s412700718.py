v1, v2, v3 = map(int, input().split())
for v4 in range(v2):
    print(v3, end=' ')
for v4 in range(v1 - v2):
    if v3 == 10 ** 9:
        print(v3 - 1, end=' ')
    else:
        print(v3 + 1, end=' ')
