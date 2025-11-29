class C1(object):

    def maxWidthRamp(self, a1):
        """
        """
        v1 = 0
        v2 = []
        for v3 in a1:
            if not v2 or a1[v2[-1]] > a1[v3]:
                v2.append(v3)
        for v4 in reversed(range(len(a1))):
            while v2 and a1[v2[-1]] <= a1[v4]:
                v1 = max(v1, v4 - v2.pop())
        return v1
