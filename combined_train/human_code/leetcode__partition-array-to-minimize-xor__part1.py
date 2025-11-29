class C1(object):

    def minXor(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = [0] * (len(a1) + 1)
        for v3 in range(len(a1)):
            v2[v3 + 1] = v2[v3] ^ a1[v3]
        v4 = v2[:]
        v4[0] = v1
        for v5 in range(2, a2 + 1):
            for v3 in reversed(range(v5 - 1, len(v4))):
                v6 = v1
                for v7 in range(v5 - 1, v3):
                    v8 = v2[v3] ^ v2[v7]
                    v9 = v4[v7] if v4[v7] > v8 else v8
                    if v9 < v6:
                        v6 = v9
                v4[v3] = v6
        return v4[-1]
