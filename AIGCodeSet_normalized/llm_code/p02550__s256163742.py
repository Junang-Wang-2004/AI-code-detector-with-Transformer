def f1():
    v1, v2, v3 = map(int, input().split())
    if v3 == 0:
        print(0)
        return
    v4 = [v2]
    v5 = -1
    for v6 in range(v1):
        v2 = v2 ** 2 % v3
        if v2 in v4:
            v5 = v2
            break
        v4.append(v2)
    v7 = v4.index(v5)
    if v7 == -1:
        print(sum(v4))
        return
    else:
        v8 = sum(v4[:v7])
        v9 = v4[v7:]
        v1 -= v7
        v8 += sum(v9) * (v1 // len(v9))
        v8 += sum(v9[:v1 % len(v9)])
        print(v8)
if __name__ == '__main__':
    f1()
