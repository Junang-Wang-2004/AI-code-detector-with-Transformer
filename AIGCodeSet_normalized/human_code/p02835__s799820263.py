def f1():
    v1, v2, v3 = map(int, input().split(' '))
    sum = v1 + v2 + v3
    if sum >= 22:
        print('bust')
    else:
        print('win')
f1()
