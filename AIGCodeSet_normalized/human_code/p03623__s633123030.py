v1, v2, v3 = (int(v1) for v1 in input().split())
if abs(v2 - v1) < abs(v3 - v1):
    print('A')
else:
    print('B')
