class C1(object):

    def maxSubarrayLength(self, a1):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x], reverse=True)
        v2 = 0
        for v3 in range(len(a1)):
            while v1 and a1[v1[-1]] < a1[v3]:
                v2 = max(v2, v1.pop() - v3 + 1)
        return v2
