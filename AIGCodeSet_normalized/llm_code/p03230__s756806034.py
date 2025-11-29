v1 = int(input())
if v1 == 1:
    print('Yes')
    print(2)
    print(1, 1)
    print(1, 1)
elif v1 == 3:
    print('Yes')
    print(3)
    print(2, 1, 2)
    print(2, 3, 1)
    print(2, 2, 3)
elif v1 % 2 == 0:
    print('Yes')
    print(v1)
    for v2 in range(1, v1 + 1, 2):
        print(2, v2, v2 + 1)
    for v2 in range(2, v1 + 1, 2):
        print(2, v2, v2 - 1)
else:
    print('No')
