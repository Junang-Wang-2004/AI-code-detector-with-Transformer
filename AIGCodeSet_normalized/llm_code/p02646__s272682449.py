v1, v2 = input().split()
v1 = int(v1)
v2 = int(v2)
v3, v4 = input().split()
v3 = int(v3)
v4 = int(v4)
v5 = int(input())
v6 = v2 - v4
v7 = abs(v1 - v3)
if v6 < 0:
    print('NO')
elif v7 < v6 * v5:
    print('NO')
else:
    print('YES')
