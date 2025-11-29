v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5 = int(input())
if (v2 - v4) * v5 >= abs(v3 - v1):
    print('YES')
else:
    print('NO')
