from collections import Counter

class C1:

    def countPairs(self, a1):
        v1 = 7
        v2 = [1]
        for v3 in range(v1 - 1):
            v2.append(v2[-1] * 10)

        def neighbors(a1):
            v1 = []
            for v2 in range(v1):
                for v3 in range(v2 + 1, v1):
                    v4 = a1 // v2[v2] % 10
                    v5 = a1 // v2[v3] % 10
                    if v4 == v5:
                        continue
                    v6 = (v5 - v4) * (v2[v2] - v2[v3])
                    v1.append(a1 + v6)
            return v1

        def get_reachable(a1):
            v1 = {a1}
            v2 = neighbors(a1)
            v1.update(v2)
            for v3 in v2:
                for v4 in neighbors(v3):
                    v1.add(v4)
            return list(v1)
        v4 = Counter(a1)
        v5 = Counter()
        v6 = 0
        for v7 in list(v4):
            v8 = v4[v7]
            v6 += v5[v7] * v8 + v8 * (v8 - 1) // 2
            v9 = get_reachable(v7)
            for v10 in v9:
                v5[v10] += v8
        return v6
