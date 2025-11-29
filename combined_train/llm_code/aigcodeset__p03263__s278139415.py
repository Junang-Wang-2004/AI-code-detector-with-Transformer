import sys

def f1():
    input = sys.stdin.readline
    v1, v2 = map(int, input().split())
    v3 = [list(map(int, input().split())) for v4 in range(v1)]
    v5 = 0
    v6 = []
    for v7 in range(v1):
        for v8 in range(v2):
            if v3[v7][v8] % 2 == 1:
                if v8 < v2 - 1 and v3[v7][v8 + 1] > 0:
                    v5 += 1
                    v6.append([v7 + 1, v8 + 1, v7 + 1, v8 + 2])
                    v3[v7][v8] -= 1
                    v3[v7][v8 + 1] -= 1
                elif v7 < v1 - 1 and v3[v7 + 1][v8] > 0:
                    v5 += 1
                    v6.append([v7 + 1, v8 + 1, v7 + 2, v8 + 1])
                    v3[v7][v8] -= 1
                    v3[v7 + 1][v8] -= 1
    print(v5)
    if v5 > 0:
        for v9 in v6:
            print('{} {} {} {}'.format(v9[0], v9[1], v9[2], v9[3]))
if __name__ == '__main__':
    f1()
