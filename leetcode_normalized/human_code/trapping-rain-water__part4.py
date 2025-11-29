class C1(object):

    def trap(self, a1):
        """
        """
        v1 = 0
        v2 = []
        for v3 in range(len(a1)):
            v4 = 0
            while v2 and a1[v2[-1]] <= a1[v3]:
                v5 = v2.pop()
                v1 += (a1[v5] - v4) * (v3 - v5 - 1)
                v4 = a1[v5]
            if v2:
                v1 += (a1[v3] - v4) * (v3 - v2[-1] - 1)
            v2.append(v3)
        return v1
