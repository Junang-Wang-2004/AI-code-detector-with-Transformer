class C1(object):

    def maxUniqueSplit(self, a1):
        """
        """

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        v1 = 1
        v2 = 2 ** (len(a1) - 1)
        v3 = 0
        while v3 < v2:
            if popcount(v3) < v1:
                v3 += 1
                continue
            v4, v5, v6 = (set(), [], v2 // 2)
            for v7 in range(len(a1)):
                v5.append(a1[v7])
                if v3 & v6 or v6 == 0:
                    if ''.join(v5) in v4:
                        v3 = (v3 | v6 - 1) + 1 if v6 else v3 + 1
                        break
                    v4.add(''.join(v5))
                    v5 = []
                v6 >>= 1
            else:
                v1 = max(v1, len(v4))
                v3 += 1
        return v1
