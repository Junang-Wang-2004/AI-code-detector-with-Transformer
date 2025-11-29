class C1(object):

    def dailyTemperatures(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = []
        for v3 in range(len(a1)):
            while v2 and a1[v2[-1]] < a1[v3]:
                v4 = v2.pop()
                v1[v4] = v3 - v4
            v2.append(v3)
        return v1
