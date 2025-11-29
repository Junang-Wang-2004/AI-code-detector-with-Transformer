def f1():
    from collections import namedtuple
    import sys
    input = sys.stdin.readline
    v1 = namedtuple('Sushi', 'x cal')
    v2, v3 = map(int, input().split())
    v4 = []
    for v5 in range(v2):
        v6, v7 = map(int, input().split())
        v4.append(v1(x=v6, cal=v7))
    v8 = [0] * (v2 + 1)
    v9 = [0] * (v2 + 1)
    v10 = 0
    v11 = 0
    v12 = 0
    for v13, v14 in enumerate(v4, start=1):
        v12 += v14.cal
        v10 = max(v10, v12 - v14.x)
        v11 = max(v11, v12 - v14.x * 2)
        v8[v13] = v10
        v9[v13] = v11
    v15 = [0] * (v2 + 1)
    v16 = [0] * (v2 + 1)
    v10 = 0
    v11 = 0
    v12 = 0
    for v13, v14 in zip(range(v2, -1, -1), reversed(v4)):
        v12 += v14.cal
        v10 = max(v10, v12 - (v3 - v14.x))
        v11 = max(v11, v12 - (v3 - v14.x) * 2)
        v15[v13] = v10
        v16[v13] = v11
    v17 = 0
    for v18 in range(1, v2 + 1):
        v17 = max(v17, v9[v18 - 1] + v15[v18], v16[(v18 + 1) % (v2 + 1)] + v8[v18])
    print(v17)
if __name__ == '__main__':
    f1()
