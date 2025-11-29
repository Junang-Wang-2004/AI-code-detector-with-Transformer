class C1(object):

    def maximumDetonation(self, a1):
        """
        """
        v1 = [[] for v2 in range(len(a1))]
        for v3, (v4, v5, v6) in enumerate(a1):
            for v7, (v8, v9, v2) in enumerate(a1):
                if v7 == v3:
                    continue
                if (v4 - v8) ** 2 + (v5 - v9) ** 2 <= v6 ** 2:
                    v1[v3].append(v7)
        v10 = 0
        for v3 in range(len(a1)):
            v11 = [v3]
            v12 = {v3}
            while v11:
                v13 = []
                for v14 in v11:
                    for v15 in v1[v14]:
                        if v15 in v12:
                            continue
                        v12.add(v15)
                        v13.append(v15)
                v11 = v13
            v10 = max(v10, len(v12))
            if v10 == len(a1):
                break
        return v10
