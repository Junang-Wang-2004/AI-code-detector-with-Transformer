def f1():
    v1 = input().rstrip()
    v2, v3, v4 = (0, 0, len(v1) - 1)
    while v3 < v4:
        if v1[v3] == v1[v4]:
            v3 += 1
            v4 -= 1
        else:
            v2 += 1
            if v1[v3] == 'x':
                v3 += 1
            elif v1[v4] == 'x':
                v4 -= 1
            else:
                print(-1)
                return
    print(v2)
if __name__ == '__main__':
    f1()
