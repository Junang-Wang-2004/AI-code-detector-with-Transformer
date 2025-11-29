def f1():
    import sys
    input = sys.stdin.readline
    v1, v2 = list(map(int, input().rstrip('\n').split()))
    v3 = [True] * (int(max(v1, v2) ** 0.5) + 1)
    v3[0] = False
    v4 = 0
    for v5 in range(len(v3)):
        if v3[v5]:
            if v1 % v5 == 0 and v2 % v5 == 0:
                v4 += 1
            if v5 != 1:
                for v6 in range(v5 * v5, len(v3), v5):
                    if v3[v6]:
                        v3[v6] = False
    print(v4)
if __name__ == '__main__':
    f1()
