class C1(object):

    def totalSteps(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = []
        for v3 in range(len(a1)):
            v4 = 0
            while v2 and a1[v2[-1]] <= a1[v3]:
                v4 = max(v4, v1[v2.pop()])
            if v2:
                v1[v3] = v4 + 1
            v2.append(v3)
        return max(v1)
