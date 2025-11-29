def f1():
    return int(input())

def f2():
    return map(int, input().split())

def f3():
    return str(input())

def f4():
    return list(input())

def f5():
    return list((int(k) for v1 in input().split()))
v1 = f1()
if v1 % 1000 == 0:
    print(0)
else:
    print(1000 - v1 % 1000)
