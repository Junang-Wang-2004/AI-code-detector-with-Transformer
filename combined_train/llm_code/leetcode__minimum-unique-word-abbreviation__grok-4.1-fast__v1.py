class C1:

    def minAbbreviation(self, a1, a2):

        def compute_length(a1, a2):
            v1 = 0
            v2 = 0
            for v3 in range(len(a1)):
                if a2 & 1 << v3:
                    if v2:
                        v1 += len(str(v2))
                    v2 = 0
                    v1 += 1
                else:
                    v2 += 1
            if v2:
                v1 += len(str(v2))
            return v1

        def construct_abbr(a1, a2):
            v1 = []
            v2 = 0
            for v3 in range(len(a1)):
                if a2 & 1 << v3:
                    if v2:
                        v1.append(str(v2))
                    v2 = 0
                    v1.append(a1[v3])
                else:
                    v2 += 1
            if v2:
                v1.append(str(v2))
            return ''.join(v1)
        v1 = len(a1)
        v2 = [sum((1 << j for v3 in range(v1) if a1[v3] != entry[v3])) for v4 in a2 if len(v4) == v1]
        v5 = (1 << v1) - 1
        v6 = v1
        v7 = v5
        for v8 in range(1 << v1):
            if all((v8 & diff != 0 for v9 in v2)):
                v10 = compute_length(a1, v8)
                if v10 < v6:
                    v6 = v10
                    v7 = v8
        return construct_abbr(a1, v7)
