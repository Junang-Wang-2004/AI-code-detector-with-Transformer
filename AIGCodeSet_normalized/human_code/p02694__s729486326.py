import sys

def f1():
    return sys.stdin.readline().rstrip()

def f2():
    v1 = int(f1())
    v2 = 0
    v3 = 100
    while True:
        v2 += 1
        v3 = int(v3 * 1.01)
        if v3 >= v1:
            print(v2)
            exit()
if __name__ == '__main__':
    f2()
