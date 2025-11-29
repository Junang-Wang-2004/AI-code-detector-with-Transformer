class C1(object):

    def minOperations(self, a1, a2):
        v1 = sorted(a1)
        v2 = len(v1)
        v3 = [0]
        for v4 in v1:
            v3.append(v3[-1] + v4)

        def get_pos(a1, a2):
            v1, v2 = (0, v2)
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if a1[v3] < a2:
                    v1 = v3 + 1
                else:
                    v2 = v3
            return v1
        v5 = []
        for v6 in a2:
            v7 = get_pos(v1, v6)
            v8 = v6 * v7 - v3[v7]
            v9 = v3[v2] - v3[v7] - v6 * (v2 - v7)
            v5.append(v8 + v9)
        return v5
