class C1:

    def sortFeatures(self, a1, a2):
        v1 = {f: 0 for v2 in a1}
        for v3 in a2:
            v4 = set(v3.split())
            for v5 in v4:
                if v5 in v1:
                    v1[v5] += 1
        v6 = [(v2, i) for v7, v2 in enumerate(a1)]
        v6.sort(key=lambda p: (-v1[p[0]], p[1]))
        return [p[0] for v8 in v6]
