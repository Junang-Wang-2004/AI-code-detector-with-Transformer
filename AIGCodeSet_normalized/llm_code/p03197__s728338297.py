v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v2 = list(set(v2))
v2.sort()
v4 = v2[-1] - v2[-2]
if v4 % 2 == 0:
    print('second')
else:
    print('first')
