class C1(object):

    def getCollisionTimes(self, a1):
        """
        """
        v1 = []
        v2 = [-1.0] * len(a1)
        for v3 in reversed(range(len(a1))):
            v4, v5 = a1[v3]
            while v1 and (a1[v1[-1]][1] >= v5 or 0 < v2[v1[-1]] <= float(a1[v1[-1]][0] - v4) / (v5 - a1[v1[-1]][1])):
                v1.pop()
            if v1:
                v2[v3] = float(a1[v1[-1]][0] - v4) / (v5 - a1[v1[-1]][1])
            v1.append(v3)
        return v2
