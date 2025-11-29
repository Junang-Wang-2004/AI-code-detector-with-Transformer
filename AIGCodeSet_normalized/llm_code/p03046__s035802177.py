v1, v2 = map(int, input().split())
v3 = 0
v4 = list(range(v2)) + list(range(v2 + 1, 2 ** v1))
if v1 == 1:
    if v2 == 0:
        print('0 0 1 1')
    else:
        print(-1)
elif 2 ** v1 - 1 > v2:
    v5 = v4 + [v2] + v4[::-1] + [v2]
    print(*v5)
else:
    print(-1)
