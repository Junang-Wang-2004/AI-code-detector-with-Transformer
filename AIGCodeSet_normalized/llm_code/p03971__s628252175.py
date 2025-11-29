v1, v2, v3 = map(int, input().split())
v4 = 0
v5 = v2 + v3
for v6 in input():
    if v6 == 'a' and v5 > 0:
        v5 -= 1
        print('YES')
    elif v6 == 'b' and v5 > 0 and (v4 < v3):
        v5 -= 1
        v4 += 1
        print('YES')
    else:
        print('NO')
