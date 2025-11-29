def f1():
    import sys
    from collections import deque
    v1 = sys.stdin.read
    v2 = sys.stdin.readline
    v3, v4, v5 = map(int, v2().split())
    v6 = map(int, v1().split())
    v7 = sorted(zip(v6, v6), key=lambda x: x[0])
    v8 = deque([])
    v9 = deque([])
    v10 = 0
    v11 = 0
    for v12, v13 in v7:
        while v8:
            v14 = v8[0]
            if v14 < v12:
                v8.popleft()
                v15 = v9.popleft()
                v10 -= v15
            else:
                break
        if v13 <= v10:
            continue
        else:
            v16 = v13 - v10
            v17 = v16 // v5 + (v16 % v5 != 0)
            v11 += v17
            v15 = v5 * v17
            v10 += v15
            v8.append(v12 + 2 * v4)
            v9.append(v15)
    print(v11)
if __name__ == '__main__':
    f1()
