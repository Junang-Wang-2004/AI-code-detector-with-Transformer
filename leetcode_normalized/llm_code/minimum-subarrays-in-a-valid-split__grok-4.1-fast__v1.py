class C1:

    def validSubarraySplit(self, a1):

        def compute_gcd(a1, a2):
            if a2 == 0:
                return a1
            return compute_gcd(a2, a1 % a2)
        v1 = len(a1)
        v2 = [float('inf')] * (v1 + 1)
        v2[0] = 0
        for v3 in range(1, v1 + 1):
            for v4 in range(v3):
                if compute_gcd(a1[v4], a1[v3 - 1]) > 1:
                    v2[v3] = min(v2[v3], v2[v4] + 1)
        v5 = v2[-1]
        return v5 if v5 < float('inf') else -1
