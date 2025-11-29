v1 = int(input())
v2 = list(map(int, input().split()))
v3 = v2[0]
v4 = v2[1]
v5 = v2[2]
if abs(v3 - v4) < abs(v3 - v5):
    print('B')
else:
    print('A')
