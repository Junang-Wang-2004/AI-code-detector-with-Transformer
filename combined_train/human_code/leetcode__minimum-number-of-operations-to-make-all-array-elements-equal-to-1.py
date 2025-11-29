class C1(object):

    def minOperations(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = a1.count(1)
        if v1:
            return len(a1) - v1
        v2 = float('inf')
        for v3 in range(len(a1)):
            v4 = a1[v3]
            for v5 in range(v3 + 1, len(a1)):
                v4 = gcd(v4, a1[v5])
                if v4 == 1:
                    v2 = min(v2, v5 - v3)
                    break
        return v2 + (len(a1) - 1) if v2 != float('inf') else -1
