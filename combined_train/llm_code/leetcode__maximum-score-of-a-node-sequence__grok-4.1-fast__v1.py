class C1(object):

    def maximumScore(self, a1, a2):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = []
        for v7 in range(v1):
            v8 = sorted(v2[v7], key=lambda x: a1[x], reverse=True)[:3]
            v6.append(v8)
        v9 = -1
        for v10, v11 in a2:
            v12 = [c for v13 in v6[v10] if v13 != v11]
            v14 = [d for v15 in v6[v11] if v15 != v10]
            for v13 in v12:
                for v15 in v14:
                    if v13 != v15:
                        v9 = max(v9, a1[v10] + a1[v11] + a1[v13] + a1[v15])
        return v9
