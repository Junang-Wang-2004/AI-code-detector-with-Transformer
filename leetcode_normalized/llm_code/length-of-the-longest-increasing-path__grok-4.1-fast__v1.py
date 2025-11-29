class C1(object):

    def maxPathLength(self, a1, a2):
        v1 = a1[a2]
        v2, v3 = (v1[0], v1[1])
        v4 = [pt for v5 in a1 if v5[0] < v2 and v5[1] < v3]
        v4.sort(key=lambda pt: (v5[0], -v5[1]))
        v6 = [v5[1] for v5 in v4]
        v7 = [v5 for v5 in a1 if v5[0] > v2 and v5[1] > v3]
        v7.sort(key=lambda pt: (v5[0], -v5[1]))
        v8 = [v5[1] for v5 in v7]

        def compute_lis_len(a1):
            if not a1:
                return 0
            v1 = []
            for v2 in a1:
                v3, v4 = (0, len(v1))
                while v3 < v4:
                    v5 = (v3 + v4) // 2
                    if v1[v5] < v2:
                        v3 = v5 + 1
                    else:
                        v4 = v5
                if v3 == len(v1):
                    v1.append(v2)
                else:
                    v1[v3] = v2
            return len(v1)
        v9 = compute_lis_len(v6)
        v10 = compute_lis_len(v8)
        return v9 + 1 + v10
