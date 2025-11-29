class C1:

    def __init__(self, a1):
        """
            data : BIT木データ
            el : 元配列
        """
        self.n = a1
        self.data = [0] * (a1 + 1)
        self.el = [0] * (a1 + 1)
    'A1 ~ Aiまでの累積和'

    def Sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.data[a1]
            a1 -= a1 & -a1
        return v1
    'Ai += x'

    def Add(self, a1, a2):
        self.el[a1] += a2
        while a1 <= self.n:
            self.data[a1] += a2
            a1 += a1 & -a1
    'Ai ~ Ajまでの累積和'

    def Get(self, a1, a2=None):
        if a2 is None:
            return self.el[a1]
        return self.Sum(a2) - self.Sum(a1)

def f4(a1):
    return ord(a1) - 97
v1 = int(input())
v2 = list(input())
v3 = int(input())
v4 = [C1(v1) for v5 in range(26)]
v6 = []
for v7 in range(v1):
    v4[f4(v2[v7])].Add(v7 + 1, 1)
for v5 in range(v3):
    v8 = list(input().split())
    if v8[0] == '1':
        v9 = int(v8[1])
        v4[f4(v2[v9 - 1])].Add(v9, -1)
        v2[v9 - 1] = v8[2]
        v4[f4(v8[2])].Add(v9, 1)
    else:
        v10, v11 = (int(v8[1]), int(v8[2]))
        v12 = 0
        for v7 in range(26):
            if v4[v7].Get(v10 - 1, v11) != 0:
                v12 += 1
        v6.append(v12)
for v13 in v6:
    print(v13)
