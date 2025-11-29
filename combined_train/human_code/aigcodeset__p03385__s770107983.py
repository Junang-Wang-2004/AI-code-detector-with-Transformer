import functools
import os
v1 = float('inf')

def f1():
    return int(input())

def f2():
    return float(input())

def f3():
    return input()

def f4():
    return list(map(int, input().split()))

def f5():
    return list(map(float, input().split()))

def f6():
    return input().split()

def f7(a1):
    if not os.getenv('LOCAL'):
        return a1

    @functools.wraps(a1)
    def wrapper(*a1, **a2):
        print('DEBUG: {}({}) -> '.format(a1.__name__, ', '.join(list(map(str, a1)) + ['{}={}'.format(k, str(v)) for v1, v2 in a2.items()])), end='')
        v3 = a1(*a1, **a2)
        print(v3)
        return v3
    return wrapper
v2 = list(input())
v2.sort()
if v2 == list('abc'):
    print('Yes')
else:
    print('No')
