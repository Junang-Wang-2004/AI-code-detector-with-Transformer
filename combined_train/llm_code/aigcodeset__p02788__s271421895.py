import sys
import bisect
sys.setrecursionlimit(10 ** 6)

class C1:

    def __init__(self, a1):
        self.N = a1
        self.data = [0] * (2 * a1)

    def update(self, a1, a2):
        a1 += self.N - 1
        self.data[a1] = a2
        while a1 > 0:
            a1 = (a1 - 1) // 2
            v2 = self.data[2 * a1 + 1] + self.data[2 * a1 + 2]
            self.data[a1] = v2

    def query(self, a1, a2, a3, a4, a5):
        if a5 <= a1 or a2 <= a4:
            return 0
        if a1 <= a4 and a5 <= a2:
            return self.data[a3]
        else:
            v1 = self.query(a1, a2, 2 * a3 + 1, a4, (a4 + a5) // 2)
            v2 = self.query(a1, a2, 2 * a3 + 2, (a4 + a5) // 2, a5)
            return v1 + v2

def f3():
    v1, v2, v3 = list(map(int, input().split(' ')))
    v4 = 1
    while v4 < v1:
        v4 *= 2
    v5 = [list(map(int, input().split(' '))) for v6 in range(v1)]
    v5.sort()
    v7 = [(h + v3 - 1) // v3 for v6, v8 in v5]
    v9 = [x for v10, v6 in v5]
    v11 = [v7[i] - v7[i - 1] if i > 0 else v7[i] for v12 in range(v1)]
    v13 = C1(v4)
    for v12, v14 in enumerate(v11):
        v13.update(v12, v14)
    v15 = 0
    for v12 in range(v1):
        v16 = v13.query(0, v12 + 1, 0, 0, v4)
        if v16 <= 0:
            continue
        v15 += v16
        v17 = v9[v12] + 2 * v2
        v18 = bisect.bisect_right(v9, v17)
        v19 = v13.query(v12, v12 + 1, 0, 0, v4)
        v20 = v13.query(v18, v18 + 1, 0, 0, v4)
        v13.update(v12, v19 - v16)
        v13.update(v18, v20 + v16)
    print(v15)
if __name__ == '__main__':
    f3()
