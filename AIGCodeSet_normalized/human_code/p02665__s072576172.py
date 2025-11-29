import sys
input = lambda: sys.stdin.readline().rstrip()

def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    if v2[0] != 0:
        if v1 == 0 and v2[0] == 1:
            print('1')
            exit()
        else:
            print('-1')
            exit()
    if v1 == 0:
        print('1')
        exit()
    v3 = [0 for v4 in range(v1 + 1)]
    v3[v1] = v2[v1]
    for v5 in range(v1 - 1, -1, -1):
        v6 = min(2 ** v5, v3[v5 + 1] + v2[v5])
        v3[v5] = v6
    for v5 in range(v1):
        v6 = min(v3[v5 + 1], (v3[v5] - v2[v5]) * 2)
        v3[v5 + 1] = v6
    v7 = 0
    for v5 in range(v1 + 1):
        if v3[v5] < v2[v5]:
            print('-1')
            exit()
        v7 += v3[v5]
    print(v7)
if __name__ == '__main__':
    f1()
