import bisect

def f1():
    v1, v2 = map(int, input().split(' '))
    v3 = []
    v4 = []
    for v5 in range(v2):
        v6, v7 = map(int, input().split(' '))
        if v6 == 1:
            v3.append(v7)
        if v7 == v1:
            v4.append(v6)
    v3 = sorted(v3)
    for v8 in v4:
        v5 = bisect.bisect_left(v3, v8)
        v9 = bisect.bisect_right(v3, v8)
        if v5 != v9:
            print('POSSIBLE')
            exit()
    print('IMPOSSIBLE')
if __name__ == '__main__':
    f1()
