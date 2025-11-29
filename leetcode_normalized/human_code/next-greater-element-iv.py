class C1(object):

    def secondGreaterElement(self, a1):
        """
        """
        v1, v2, v3 = ([-1] * len(a1), [], [])
        for v4, v5 in enumerate(a1):
            while v3 and a1[v3[-1]] < v5:
                v1[v3.pop()] = v5
            v6 = []
            while v2 and a1[v2[-1]] < v5:
                v6.append(v2.pop())
            v2.append(v4)
            for v5 in reversed(v6):
                v3.append(v5)
        return v1
