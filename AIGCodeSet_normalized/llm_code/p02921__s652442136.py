def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    assert len(v2) == v1
    v3 = 999999
    for v4 in v2:
        v3 = min(v3, f2(v4))
    print(v3)

def f2(a1):
    for v1 in range(10000):
        if a1 % 2 ** v1 != 0:
            break
    assert v1 >= 1
    return v1 - 1
if __name__ == '__main__':
    f1()
