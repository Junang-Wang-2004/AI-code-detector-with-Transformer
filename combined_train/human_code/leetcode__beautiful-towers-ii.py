class C1(object):

    def maximumSumOfHeights(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = [-1]
        v3 = 0
        for v4 in range(len(a1)):
            while v2[-1] != v2[0] and a1[v2[-1]] >= a1[v4]:
                v5 = v2.pop()
                v3 -= (v5 - v2[-1]) * a1[v5]
            v3 += (v4 - v2[-1]) * a1[v4]
            v2.append(v4)
            v1[v4] = v3
        v2 = [len(a1)]
        v6 = v7 = v3 = 0
        for v4 in reversed(range(len(a1))):
            while v2[-1] != v2[0] and a1[v2[-1]] >= a1[v4]:
                v5 = v2.pop()
                v3 -= (v2[-1] - v5) * a1[v5]
            v3 += (v2[-1] - v4) * a1[v4]
            v2.append(v4)
            v7 = v3
            v6 = max(v6, v1[v4] + v7 - a1[v4])
        return v6
