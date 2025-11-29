class C1(object):

    def maximumLengthOfRanges(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = [-1]
        a1.append(float('inf'))
        for v3, v4 in enumerate(a1):
            while v2[-1] != -1 and a1[v2[-1]] < v4:
                v5 = v2.pop()
                v1[v5] = v3 - 1 - v2[-1]
            v2.append(v3)
        return v1
