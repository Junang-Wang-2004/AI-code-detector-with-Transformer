class C1(object):

    def waysToSplit(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0]
        for v3 in a1:
            v2.append(v2[-1] + v3)
        v4 = v5 = v6 = 0
        for v7 in range(len(a1)):
            v5 = max(v5, v7 + 1)
            while v5 + 1 < len(a1) and v2[v7 + 1] > v2[v5 + 1] - v2[v7 + 1]:
                v5 += 1
            v6 = max(v6, v5)
            while v6 + 1 < len(a1) and v2[v6 + 1] - v2[v7 + 1] <= v2[-1] - v2[v6 + 1]:
                v6 += 1
            v4 = (v4 + (v6 - v5)) % v1
        return v4
