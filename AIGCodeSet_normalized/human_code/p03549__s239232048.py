def f1(a1: int, a2: int) -> int:
    v1 = (1900 * a2 + (a1 - a2) * 100) * 2 ** a2
    return v1

def f2():
    return

def f3():
    v1, v2 = map(int, input().split())
    print(f1(v1, v2))
if __name__ == '__main__':
    f3()
