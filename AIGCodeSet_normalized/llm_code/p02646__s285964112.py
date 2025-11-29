v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5 = int(input())
if abs(v1 - v3) <= abs(v2 - v4) * v5:
    print('Yes')
else:
    print('No')
