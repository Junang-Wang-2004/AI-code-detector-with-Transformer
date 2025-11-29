class C1:

    def peopleIndexes(self, a1):
        v1 = {}
        v2 = 0
        v3 = []
        for v4 in a1:
            v5 = []
            for v6 in v4:
                if v6 not in v1:
                    v1[v6] = v2
                    v2 += 1
                v5.append(v1[v6])
            v3.append(sorted(set(v5)))

        def strict_subset(a1, a2):
            if len(a1) >= len(a2):
                return False
            v1 = v2 = 0
            while v1 < len(a1) and v2 < len(a2):
                if a1[v1] == a2[v2]:
                    v1 += 1
                    v2 += 1
                elif a1[v1] < a2[v2]:
                    return False
                else:
                    v2 += 1
            return v1 == len(a1)
        v7 = len(v3)
        v8 = []
        for v9 in range(v7):
            v10 = False
            for v11 in range(v7):
                if v9 == v11 or len(v3[v11]) <= len(v3[v9]):
                    continue
                if strict_subset(v3[v9], v3[v11]):
                    v10 = True
                    break
            if not v10:
                v8.append(v9)
        return v8
