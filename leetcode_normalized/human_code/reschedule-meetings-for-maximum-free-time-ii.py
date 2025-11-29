class C1(object):

    def maxFreeTime(self, a1, a2, a3):
        """
        """

        def topk(a1, a2):
            v1 = [[float('-inf')] * 2 for v2 in range(a2)]
            for v3 in a1:
                for v4 in range(len(v1)):
                    if v3 > v1[v4]:
                        v1[v4], v3 = (v3, v1[v4])
            return v1
        v1 = 0
        a2.append(a1)
        a3.insert(0, 0)
        v2 = ([a2[i] - a3[i], a3[i]] for v3 in range(len(a2)))
        v4 = topk(v2, 3)
        for v3 in range(len(a2) - 1):
            for v5, v6 in v4:
                if v6 not in (a3[v3], a3[v3 + 1]) and a3[v3 + 1] - a2[v3] <= v5:
                    v1 = max(v1, a2[v3] - a3[v3] + (a2[v3 + 1] - a3[v3 + 1]) + (a3[v3 + 1] - a2[v3]))
                    break
            else:
                v1 = max(v1, a2[v3] - a3[v3] + (a2[v3 + 1] - a3[v3 + 1]))
        return v1
