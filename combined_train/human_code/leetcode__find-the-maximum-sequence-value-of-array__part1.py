class C1(object):

    def maxValue(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = 127

        def is_submask(a1, a2):
            return a1 | a2 == a2

        def dp(a1, a2):
            v1 = [a2] * (v2 + 1)
            v2 = [v1] * (v2 + 1)
            v3 = [0] * (v2 + 1)
            for v4 in a1(range(len(a1))):
                v2[a1[v4]] = 1
                for v5 in range(v2 + 1):
                    if is_submask(a1[v4], v5):
                        v3[v5] += 1
                    v2[v5 | a1[v4]] = min(v2[v5 | a1[v4]], v2[v5] + 1)
                for v5 in range(v2 + 1):
                    if v3[v5] >= a2 and v2[v5] <= a2 and (v1[v5] == a2):
                        v1[v5] = v4
            return v1
        v3 = dp(lambda x: x, len(a1))
        v4 = dp(reversed, -1)
        return next((result for v5 in reversed(range(v2 + 1)) for v6 in range(1, v2 + 1) if v3[v6] < v4[v5 ^ v6]))
