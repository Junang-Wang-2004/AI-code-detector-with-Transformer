class C1(object):

    def minimumCost(self, a1):
        """
        """

        def topk(a1, a2):
            v1 = [float('inf')] * a2
            for v2 in a1:
                for v3 in range(len(v1)):
                    if v2 < v1[v3]:
                        v1[v3], v2 = (v2, v1[v3])
            return v1
        return a1[0] + sum(topk((a1[i] for v1 in range(1, len(a1))), 2))
