class C1(object):

    def validSubarraySplit(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = [float('inf')] * (len(a1) + 1)
        v1[0] = 0
        for v2 in range(1, len(a1) + 1):
            for v3 in range(v2):
                if gcd(a1[v3], a1[v2 - 1]) != 1:
                    v1[v2] = min(v1[v2], v1[v3] + 1)
        return v1[-1] if v1[-1] != float('inf') else -1
