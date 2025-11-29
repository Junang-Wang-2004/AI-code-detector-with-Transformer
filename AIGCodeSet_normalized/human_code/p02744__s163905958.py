v1 = int(input())
v2 = 'abcdefghijklmmopkrstuvwxyz'

def f1(a1, a2):
    if len(a1) == v1:
        print(a1)
        return
    for v1 in v2:
        if ord(v1) - a2 <= 1:
            f1(a1 + v1, max(a2, ord(v1)))
f1('a', ord('a'))
