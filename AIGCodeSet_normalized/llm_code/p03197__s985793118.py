v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
if v1 == 2 and min(v2) == 1:
    print('first')
elif sum(v2) % 2 == 1:
    print('first')
else:
    print('second')
