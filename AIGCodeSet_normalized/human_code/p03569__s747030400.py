def f1():
    v1 = input()
    v2 = 0
    v3 = len(v1) - 1
    v4 = 0
    while v2 < v3:
        if v1[v2] == v1[v3]:
            v2 += 1
            v3 -= 1
            continue
        if v1[v2] == 'x':
            v2 += 1
            v4 += 1
            continue
        if v1[v3] == 'x':
            v3 -= 1
            v4 += 1
            continue
        print(-1)
        return
    print(v4)
if __name__ == '__main__':
    f1()
