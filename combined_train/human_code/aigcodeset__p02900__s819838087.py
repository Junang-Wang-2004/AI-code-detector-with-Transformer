def f1():
    v1, v2 = list(map(int, input().split()))

    def factorization(a1):
        v1 = set()
        v2 = 0
        v3 = a1
        for v4 in range(2, int(a1 ** 0.5) + 1):
            if v3 % v4 == 0:
                v2 = 0
                while v3 % v4 == 0:
                    v2 += 1
                    v3 /= v4
                v1.add(v4)
        if v3 != 1:
            v1.add(int(v3))
        if v1 == []:
            v1.add(a1)
        return v1
    print(len(factorization(v1) & factorization(v2)) + 1)
if __name__ == '__main__':
    f1()
