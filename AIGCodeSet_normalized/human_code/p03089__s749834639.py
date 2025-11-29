import sys
input = sys.stdin.readline
v1 = enumerate
v2 = 1001001001

def f1(a1=int, a2=list):
    return a2(map(a1, input().rstrip().split()))

def f2(a1=1, a2=int, a3=list):
    return a3((a2(input().rstrip()) for v1 in '*' * a1))

def f3(a1: int, a2: int):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f4(a1: int, a2: int):
    return a1 * a2 // f3(a1, a2)

def f5():
    v1, = f1()
    v2 = f1()
    v3 = [b - i - 1 for v4, v5 in v1(v2)]
    v3.reverse()
    v6 = 0
    v7 = []
    for v8 in '*' * v1:
        try:
            v9 = v3.index(0)
            v7.append(v2[v1 - v9 - 1])
            v3[v9] = -v2
            for v10 in range(v9):
                v3[v10] += 1
        except ValueError as v11:
            print(-1)
            return
    print(*v7[::-1], sep='\n')
if __name__ == '__main__':
    f5()
