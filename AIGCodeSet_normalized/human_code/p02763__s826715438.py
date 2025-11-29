def f1():
    v1 = int(input())
    v2 = ord('a')
    v3 = lambda x: ord(x) - v2
    v4 = list(map(v3, list(input())))
    v5 = int(input())
    v6 = [C1(v1) for v7 in range(26)]
    for v8, v9 in enumerate(v4, 1):
        v6[v9].add(v8, 1)
    for v7 in range(v5):
        v10, v8, v11 = input().split()
        v8 = int(v8)
        if v10 == '1':
            v6[v4[v8 - 1]].add(v8, -1)
            v6[ord(v11) - v2].add(v8, 1)
            v4[v8 - 1] = ord(v11) - v2
        else:
            v11 = int(v11)
            v12 = 0
            for v13 in v6:
                v14 = v13.sum_(v11) - v13.sum_(v8 - 1)
                if v14:
                    v12 += 1
            print(v12)

class C1:
    __slots__ = ['length', 'data']

    def __init__(self, a1):
        self.data = [0] * (a1 + 1)
        self.length = a1

    def add(self, a1, a2):
        while a1 < self.length + 1:
            self.data[a1] += a2
            a1 += a1 & -a1

    def sum_(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.data[a1]
            a1 -= a1 & -a1
        return v1
if __name__ == '__main__':
    f1()
