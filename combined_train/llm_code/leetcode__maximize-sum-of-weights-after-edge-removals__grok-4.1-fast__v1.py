class C1:

    def maximizeSumOfWeights(self, a1, a2):
        v1 = len(a1) + 1
        v2 = [[] for v3 in range(v1)]
        for v4, v5, v6 in a1:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))

        def explore(a1, a2):
            v1 = 0
            v2 = []
            for v3, v4 in v2[a1]:
                if v3 == a2:
                    continue
                v5, v6 = explore(v3, a1)
                v1 += v5
                v7 = max(v6 + v4 - v5, 0)
                v2.append(v7)
            v2.sort(reverse=True)
            v8 = min(a2, len(v2))
            v9 = max(0, min(a2 - 1, len(v2)))
            v10 = v1 + sum(v2[:v8])
            v11 = v1 + sum(v2[:v9])
            return (v10, v11)
        return explore(0, -1)[0]
