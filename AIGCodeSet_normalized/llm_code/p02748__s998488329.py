import sys

def f1():
    input = sys.stdin.readline
    v1, v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = list(map(int, input().split()))
    v5 = [list(map(int, input().split())) for v1 in range(v2)]
    v6 = []
    for v7 in v3:
        for v8 in v4:
            v6.append(v7 + v8)
    for v9 in range(v2):
        v6.append(v3[v5[v9][0] - 1] + v4[v5[v9][1] - 1] - v5[v9][2])
    print(min(v6))
if __name__ == '__main__':
    f1()
