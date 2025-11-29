class C1(object):

    def maximalPathQuality(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = [0] * v1

        def traverse(a1, a2, a3):
            v7[a1] += 1
            v1 = a3 + (a1[a1] if v7[a1] == 1 else 0)
            v2 = v1 if a1 == 0 else 0
            for v3, v4 in v2[a1]:
                v5 = (a1, v3)
                if a2 < v4 or v5 in used_edges:
                    continue
                used_edges.add(v5)
                v2 = max(v2, traverse(v3, a2 - v4, v1))
                used_edges.remove(v5)
            v7[a1] -= 1
            return v2
        v8 = set()
        return traverse(0, a3, 0)
