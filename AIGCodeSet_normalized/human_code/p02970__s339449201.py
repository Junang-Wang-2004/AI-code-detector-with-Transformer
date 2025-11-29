def f1():
    v1, v2 = map(int, input().split(' '))
    v3 = v2 * 2 + 1
    for v4 in range(1, v1 + 1):
        if v1 / (v4 * v3) <= 1:
            print(v4)
            break
if __name__ == '__main__':
    f1()
