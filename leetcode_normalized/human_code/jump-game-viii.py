class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1, v2 = ([], [])
        v3 = [float('inf')] * len(a1)
        v3[0] = 0
        for v4 in range(len(a1)):
            while v1 and a1[v1[-1]] <= a1[v4]:
                v3[v4] = min(v3[v4], v3[v1.pop()] + a2[v4])
            v1.append(v4)
            while v2 and a1[v2[-1]] > a1[v4]:
                v3[v4] = min(v3[v4], v3[v2.pop()] + a2[v4])
            v2.append(v4)
        return v3[-1]
