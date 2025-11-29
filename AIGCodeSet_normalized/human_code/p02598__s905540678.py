import sys

def f1():
    return sys.stdin.readline().rstrip()

def f2(a1, a2):
    return (a1 - 1) // a2

def f3(a1, a2, a3):
    v1 = map(lambda x: f2(x, a1), a2)
    return sum(v1) <= a3

def f4(a1, a2, a3, a4):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(a2 - a1) > 1:
        v1 = (a2 + a1) // 2
        if f3(v1, a3, a4):
            a2 = v1
        else:
            a1 = v1
    return a2

def f5():
    v1, v2 = map(int, f1().split())
    v3 = list(map(int, f1().split()))
    print(f4(0, 10 ** 9 + 1, v3, v2))
if __name__ == '__main__':
    f5()
