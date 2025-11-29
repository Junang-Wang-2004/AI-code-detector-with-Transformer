class C1(object):

    def minXor(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = [0] * (len(a1) + 1)
        for v3 in range(len(a1)):
            v2[v3 + 1] = v2[v3] ^ a1[v3]
        v4 = [v1] * (len(a1) + 1)
        v4[0] = 0
        for v5 in range(1, a2 + 1):
            for v3 in reversed(range(v5 - 1, len(v4))):
                v4[v3] = v1
                for v6 in range(v5 - 1, v3):
                    v4[v3] = min(v4[v3], max(v4[v6], v2[v3] ^ v2[v6]))
        return v4[-1]
