class C1(object):

    def maximumBooks(self, a1):
        """
        """

        def count(a1, a2):
            v1 = max(a1 - a2 + 1, 0)
            return (v1 + a1) * (a1 - v1 + 1) // 2
        v1 = v2 = 0
        v3 = [-1]
        for v4 in range(len(a1)):
            while v3[-1] != -1 and a1[v3[-1]] >= a1[v4] - (v4 - v3[-1]):
                v5 = v3.pop()
                v2 -= count(a1[v5], v5 - v3[-1])
            v2 += count(a1[v4], v4 - v3[-1])
            v3.append(v4)
            v1 = max(v1, v2)
        return v1
