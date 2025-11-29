class C1:

    def beautifulIndices(self, a1, a2, a3, a4):

        def compute_failure(a1):
            v1 = len(a1)
            v2 = [0] * v1
            v3 = 0
            v4 = 1
            while v4 < v1:
                if a1[v4] == a1[v3]:
                    v3 += 1
                    v2[v4] = v3
                    v4 += 1
                elif v3 > 0:
                    v3 = v2[v3 - 1]
                else:
                    v2[v4] = 0
                    v4 += 1
            return v2

        def extract_starts(a1, a2):
            v1 = []
            if len(a2) > len(a1):
                return v1
            v2 = compute_failure(a2)
            v3 = 0
            for v4 in range(len(a1)):
                while v3 > 0 and a2[v3] != a1[v4]:
                    v3 = v2[v3 - 1]
                if a2[v3] == a1[v4]:
                    v3 += 1
                if v3 == len(a2):
                    v1.append(v4 - len(a2) + 1)
                    v3 = v2[v3 - 1]
            return v1
        v1 = extract_starts(a1, a2)
        v2 = extract_starts(a1, a3)
        v3 = []
        v4 = 0
        for v5 in v1:
            while v4 < len(v2) and v2[v4] < v5 - a4:
                v4 += 1
            if v4 < len(v2) and v2[v4] <= v5 + a4:
                v3.append(v5)
        return v3
