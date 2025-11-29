class C1(object):

    def mctFromLeafValues(self, a1):
        """
        """
        v1 = 0
        v2 = [float('inf')]
        for v3 in a1:
            while v2[-1] <= v3:
                v1 += v2.pop() * min(v2[-1], v3)
            v2.append(v3)
        while len(v2) > 2:
            v1 += v2.pop() * v2[-1]
        return v1
