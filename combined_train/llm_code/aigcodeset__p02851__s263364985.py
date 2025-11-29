import sys

def f1():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = [0] * (v1 + 1)
    v5 = 0
    for v6, v7 in enumerate(v3):
        v5 += v7
        v4[v6 + 1] = v5 % v2
    v8 = 0
    v9 = [0] * v2
    for v10 in range(v1 + 1):
        v11 = v4[v10]
        if v10 - v2 >= 0:
            v9[v4[v10 - v2]] -= 1
        v8 += v9[v11]
        v9[v11] += 1
    print(v8)
v1 = False

def f2(a1):
    if v1:
        print(a1)
if __name__ == '__main__':
    if sys.platform == 'ios':
        sys.stdin = open('inputFile.txt')
        v1 = True
    else:
        pass
    v2 = f1()
    if v2 is not None:
        print(v2)
