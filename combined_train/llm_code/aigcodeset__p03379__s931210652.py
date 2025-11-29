import sys
input = sys.stdin.readline

def f1(a1):
    a1 = sorted(a1)
    if len(a1) % 2 == 1:
        return a1[len(a1) // 2]
    else:
        return (a1[len(a1) // 2] + a1[len(a1) // 2 - 1]) // 2

def f2():
    v1 = int(input().strip())
    v2 = [int(i) for v3 in input().strip().split()]
    v4 = 0
    v5 = sorted(v2)
    v6 = v5[v1 // 2 - 1]
    v7 = v5[v1 // 2]
    for v8 in v2:
        if v8 >= v7:
            print(v7)
        else:
            print(v6)
if __name__ == '__main__':
    f2()
