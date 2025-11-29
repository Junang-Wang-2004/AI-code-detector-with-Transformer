import sys
v1 = []
v1 = input().rstrip().split(' ')
v2 = int(v1[0])
v3 = int(v1[1])
print('100 100')
for v4 in range(50):
    for v5 in range(100):
        if v4 == 0:
            print('.', end='')
            if v5 == 99:
                print()
            continue
        if v5 == 0:
            print('.', end='')
            continue
        elif v5 == 99:
            print('.', end='')
            print()
            continue
        else:
            v6 = v4 % 2
            v7 = v5 % 2
            if v6 == 1 and v7 == 1 and (v3 > 1):
                print('#', end='')
                v3 -= 1
            else:
                print('.', end='')
for v4 in range(50):
    for v5 in range(100):
        if v4 == 0:
            print('#', end='')
            if v5 == 99:
                print()
            continue
        if v5 == 0:
            print('#', end='')
            continue
        elif v5 == 99:
            print('#', end='')
            print()
            continue
        else:
            v6 = v4 % 2
            v7 = v5 % 2
            if v6 == 1 and v7 == 1 and (v2 > 1):
                print('.', end='')
                v2 -= 1
            else:
                print('#', end='')
