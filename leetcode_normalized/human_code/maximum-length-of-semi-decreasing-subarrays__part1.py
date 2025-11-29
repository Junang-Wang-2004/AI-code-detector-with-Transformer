class C1(object):

    def maxSubarrayLength(self, a1):
        """
        """
        v1 = []
        for v2 in reversed(range(len(a1))):
            if not v1 or a1[v1[-1]] > a1[v2]:
                v1.append(v2)
        v3 = 0
        for v4 in range(len(a1)):
            while v1 and a1[v1[-1]] < a1[v4]:
                v3 = max(v3, v1.pop() - v4 + 1)
        return v3
