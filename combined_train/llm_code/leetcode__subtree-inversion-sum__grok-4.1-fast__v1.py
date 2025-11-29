class C1(object):

    def subtreeInversionSum(self, a1, a2, a3):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = []

        def traverse(a1, a2):
            v6.append([0, 0])
            v1 = a2[a1]
            v2 = 0
            v3 = 0
            for v4 in v2[a1]:
                if v4 == a2:
                    continue
                v5, v6, v7 = traverse(v4, a1)
                v1 += v5
                v2 += v6
                v3 += v7
            v2 = max(v2, v6[-1][1] - 2 * v1)
            v3 = max(v3, v6[-1][0] + 2 * v1)
            v6.pop()
            v8 = len(v6)
            if v8 >= a3:
                v6[v8 - a3][0] += v2
                v6[v8 - a3][1] += v3
            return (v1, v2, v3)
        v7, v8, v3 = traverse(0, -1)
        return v7 + v8
