class C1(object):

    def findMaximums(self, a1):
        """
        """

        def find_bound(a1, a2, a3):
            v1 = [0] * len(a1)
            v2 = [a3]
            for v3 in a2(range(len(a1))):
                while v2[-1] != a3 and a1[v2[-1]] >= a1[v3]:
                    v2.pop()
                v1[v3] = v2[-1]
                v2.append(v3)
            return v1
        v1 = find_bound(a1, lambda x: x, -1)
        v2 = find_bound(a1, reversed, len(a1))
        v3 = [-1] * len(a1)
        for v4, v5 in enumerate(a1):
            v3[v2[v4] - 1 - v1[v4] - 1] = max(v3[v2[v4] - 1 - v1[v4] - 1], v5)
        for v4 in reversed(range(len(a1) - 1)):
            v3[v4] = max(v3[v4], v3[v4 + 1])
        return v3
