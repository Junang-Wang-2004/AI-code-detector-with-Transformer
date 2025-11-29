def f1():
    return int(input())

def f2():
    return [int(i) for v1 in input().split()]
v1 = f2()
v1.sort()
if v1 == [1, 4, 7, 9]:
    print('YES')
else:
    print('NO')
