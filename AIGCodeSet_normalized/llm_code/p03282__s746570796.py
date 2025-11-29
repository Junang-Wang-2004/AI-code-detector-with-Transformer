import sys

def f1():
    return int(sys.stdin.readline())

def f2():
    return map(int, sys.stdin.readline().split())

def f3():
    return list(map(int, sys.stdin.readline().split()))

def f4():
    v1 = input()
    v2 = f1()
    for v3 in v1:
        if v3 != '1':
            print(v3)
            sys.exit()
    print(1)
if __name__ == '__main__':
    f4()
