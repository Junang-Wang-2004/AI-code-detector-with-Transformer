def f1(a1: int) -> int:
    """n を素因数分解した時の 2 の指数
    """
    v1 = 0
    while a1 % 2 == 0:
        v1 += 1
        a1 //= 2
    return v1

def f2(a1: int, a2: list) -> int:
    return sum((f1(a) for v1 in a2))
if __name__ == '__main__':
    v1 = int(input())
    v2 = [int(s) for v3 in input().split()]
    v4 = f2(v1, v2)
    print(v4)
