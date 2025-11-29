class C1:

    def __init__(self):
        self.children = {}

class C2:

    def distinctSubarraysWithAtMostKOddIntegers(self, a1, a2):
        v1 = C1()
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = len(a1)
        for v6 in range(v5):
            v4 += a1[v6] % 2
            while v4 > a2:
                v4 -= a1[v3] % 2
                v3 += 1
            v7 = v1
            v8 = 0
            for v9 in range(v6, v3 - 1, -1):
                v10 = a1[v9]
                if v10 not in v7.children:
                    v8 += 1
                    v7.children[v10] = C1()
                v7 = v7.children[v10]
            v2 += v8
        return v2
