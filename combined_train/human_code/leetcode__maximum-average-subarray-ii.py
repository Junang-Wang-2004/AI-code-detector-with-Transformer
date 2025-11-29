class C1(object):

    def findMaxAverage(self, a1, a2):
        """
        """

        def getDelta(a1, a2, a3):
            v1 = [0.0] * (len(a2) + 1)
            v2 = None
            v3 = 0.0
            for v4 in range(len(a2)):
                v1[v4 + 1] = a2[v4] + v1[v4] - a1
                if v4 >= a3 - 1:
                    if v2 == None or v1[v4 - a3 + 1] < v1[v2]:
                        v2 = v4 - a3 + 1
                    if v1[v4 + 1] - v1[v2] >= 0:
                        v3 = max(v3, (v1[v4 + 1] - v1[v2]) / (v4 + 1 - v2))
            return v3
        v1, v2 = (min(a1), float('inf'))
        while v2 > 1e-05:
            v2 = getDelta(v1, a1, a2)
            v1 += v2
        return v1
