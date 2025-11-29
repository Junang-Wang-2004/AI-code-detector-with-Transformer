def f1():
    import sys
    input = sys.stdin.buffer.readline
    v1, v2 = (int(i) for v3 in input().split())
    v4 = [int(v3) for v3 in input().split()]
    v4.sort(reverse=True)
    v5 = [[int(v3) for v3 in input().split()] for v6 in range(v2)]
    v5.sort(key=lambda p: p[1], reverse=True)
    v7 = 0
    v8 = False
    for v9, v10 in v5:
        for v3 in range(v9):
            if v4 and v4[-1] < v10:
                v4.pop()
                v7 += v10
            else:
                v8 = True
                break
        if v8:
            break
    print(sum(v4) + v7)
if __name__ == '__main__':
    f1()
