import collections

class C1:

    def maxAmount(self, a1, a2, a3, a4, a5):

        def setup_links(a1, a2):
            v1 = collections.defaultdict(list)
            for v2 in range(len(a1)):
                v3, v4 = a1[v2]
                v5 = a2[v2]
                v1[v3].append((v4, v5))
                v1[v4].append((v3, 1.0 / v5))
            return v1

        def spread_values(a1, a2):
            v1 = list(a1.keys())
            while v1:
                v2 = []
                for v3 in v1:
                    for v4, v5 in a2[v3]:
                        v6 = a1[v3] * v5
                        if v6 > a1[v4]:
                            a1[v4] = v6
                            v2.append(v4)
                v1 = v2
        v1 = collections.defaultdict(float)
        v1[a1] = 1.0
        v2 = setup_links(a2, a3)
        spread_values(v1, v2)
        v3 = [[y, x] for v4, v5 in a4]
        v6 = setup_links(v3, a5)
        v7 = collections.defaultdict(float)
        v7[a1] = 1.0
        spread_values(v7, v6)
        v8 = 0.0
        for v9 in v1:
            v8 = max(v8, v1[v9] * v7[v9])
        return v8
