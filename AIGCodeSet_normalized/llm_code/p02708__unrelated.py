v1 = 10 ** 9 + 7

def f1():
    v1, v2 = map(int, input().split())
    if v2 == 1:
        v3 = 1
    elif v2 == v1 + 1:
        v3 = 1
    else:
        v3 = (v1 - v2 + 1) * (v1 - v2 + 2) // 2 % v1
    print(v3)
if __name__ == '__main__':
    f1()
