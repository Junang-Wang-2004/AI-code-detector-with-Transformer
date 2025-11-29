class C1(object):

    def minOperations(self, a1):
        """
        """

        def unique(a1):
            v1 = 0
            for v2 in range(1, len(a1)):
                if a1[v1] != a1[v2]:
                    v1 += 1
                    a1[v1] = a1[v2]
            return v1

        def erase(a1, a2):
            while len(a1) > a2 + 1:
                a1.pop()
        v1 = len(a1)
        a1.sort()
        erase(a1, unique(a1))
        v2 = v3 = 0
        for v4 in range(len(a1)):
            if a1[v4] <= a1[v4 - v3] + v1 - 1:
                v3 += 1
        return v1 - v3
