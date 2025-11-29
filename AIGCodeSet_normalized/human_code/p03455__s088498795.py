def f1(a1, a2):
    if a1 * a2 % 2 == 0:
        print('Even')
    else:
        print('Odd')
v1, v2 = map(int, input().split())
f1(v1, v2)
