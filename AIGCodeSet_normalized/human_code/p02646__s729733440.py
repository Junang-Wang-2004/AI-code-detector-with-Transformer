def f1():
    v1, v2 = [int(i) for v3 in input().split()]
    v4, v5 = [int(v3) for v3 in input().split()]
    v6 = int(input())
    if v2 <= v5:
        print('NO')
    elif (v2 - v5) * v6 < abs(v1 - v4):
        print('NO')
    else:
        print('YES')
f1()
