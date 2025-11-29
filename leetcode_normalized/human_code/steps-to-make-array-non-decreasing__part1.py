class C1(object):

    def totalSteps(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = []
        for v3 in reversed(range(len(a1))):
            while v2 and a1[v2[-1]] < a1[v3]:
                v1[v3] = max(v1[v3] + 1, v1[v2.pop()])
            v2.append(v3)
        return max(v1)
