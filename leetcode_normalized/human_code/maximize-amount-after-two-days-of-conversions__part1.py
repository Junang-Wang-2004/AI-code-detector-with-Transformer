class C1(object):

    def maxAmount(self, a1, a2, a3, a4, a5):
        """
        """

        def BellmanFord(a1, a2, a3):
            for v1 in range(len(a2)):
                for v2 in range(len(a2)):
                    a1[a2[v2][1]] = max(a1[a2[v2][1]], a1[a2[v2][0]] * a3[v2])
                    a1[a2[v2][0]] = max(a1[a2[v2][0]], a1[a2[v2][1]] * (1 / a3[v2]))
        v1 = collections.defaultdict(int)
        v1[a1] = 1.0
        BellmanFord(v1, a2, a3)
        BellmanFord(v1, a4, a5)
        return v1[a1]
