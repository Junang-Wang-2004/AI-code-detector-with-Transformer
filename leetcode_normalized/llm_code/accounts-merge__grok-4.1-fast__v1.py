from collections import defaultdict

class C1:

    def accountsMerge(self, a1):
        v1 = {}
        v2 = {}
        v3 = {}

        def find(a1):
            if v1[a1] != a1:
                v1[a1] = find(v1[a1])
            return v1[a1]

        def unite(a1, a2):
            v1 = find(a1)
            v2 = find(a2)
            if v1 == v2:
                return
            if v2[v1] < v2[v2]:
                v1[v1] = v2
            elif v2[v1] > v2[v2]:
                v1[v2] = v1
            else:
                v1[v2] = v1
                v2[v1] += 1
        for v4 in a1:
            v5 = v4[0]
            v6 = v4[1:]
            if v6:
                v7 = v6[0]
                for v8 in v6:
                    if v8 not in v1:
                        v1[v8] = v8
                        v2[v8] = 0
                        v3[v8] = v5
                for v8 in v6[1:]:
                    unite(v7, v8)
        v9 = defaultdict(list)
        for v8 in v1:
            v9[find(v8)].append(v8)
        v10 = []
        for v11 in v9.values():
            v11.sort()
            v10.append([v3[v11[0]]] + v11)
        return v10
