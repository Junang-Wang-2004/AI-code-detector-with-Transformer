v1, v2, v3 = list(map(int, input().split()))
if abs(v1 - v2) > abs(v1 - v3):
    print('B')
else:
    print('A')
