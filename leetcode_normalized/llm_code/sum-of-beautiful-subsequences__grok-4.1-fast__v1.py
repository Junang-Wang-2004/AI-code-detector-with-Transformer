v1 = 10 ** 9 + 7

class C1:

    def __init__(self, a1):
        self.capacity = a1
        self.data = [0] * (a1 + 2)

    def modify(self, a1, a2):
        a1 += 1
        while a1 <= self.capacity:
            self.data[a1] = (self.data[a1] + a2) % v1
            a1 += a1 & -a1

    def accumulate(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 = (v2 + self.data[a1]) % v1
            a1 -= a1 & -a1
        return v2

class C2:

    def totalBeauty(self, a1):
        if not a1:
            return 0
        v1 = max(a1)
        v2 = [[] for v3 in range(v1 + 1)]
        for v4 in a1:
            v5 = []
            v6 = 1
            while v6 * v6 <= v4:
                if v4 % v6 == 0:
                    v5.append(v6)
                    if v6 != v4 // v6:
                        v5.append(v4 // v6)
                v6 += 1
            for v7 in v5:
                v2[v7].append(v4)
        v8 = list(range(v1 + 1))
        for v9 in range(2, v1 + 1):
            if v8[v9] == v9:
                for v10 in range(v9, v1 + 1, v9):
                    v8[v10] = v8[v10] // v9 * (v9 - 1)
        v11 = 0
        for v6 in range(1, v1 + 1):
            v12 = v2[v6]
            if not v12:
                continue
            v13 = sorted(set(v12))
            v14 = {value: pos for v15, v16 in enumerate(v13)}
            v17 = len(v13)
            v18 = C1(v17)
            for v16 in v12:
                v15 = v14[v16]
                v19 = v18.accumulate(v15 - 1) if v15 > 0 else 0
                v20 = (v19 + 1) % v1
                v18.modify(v15, v20)
            v21 = v18.accumulate(v17 - 1)
            v11 = (v11 + v8[v6] * v21) % v1
        return v11
