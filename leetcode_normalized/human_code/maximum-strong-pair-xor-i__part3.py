class C1(object):

    def maximumStrongPairXor(self, a1):
        """
        """
        v1 = 0
        for v2 in reversed(range(max(a1).bit_length())):
            v3, v4 = ({}, {})
            for v5 in a1:
                v6 = v5 >> v2
                if v6 not in v3:
                    v3[v6] = v4[v6] = v5
                v3[v6] = min(v3[v6], v5)
                v4[v6] = max(v4[v6], v5)
            v1 <<= 1
            for v5 in v3.keys():
                v6 = (v1 | 1) ^ v5
                assert v5 != v6
                if v6 in v4 and v3[max(v5, v6)] <= 2 * v4[min(v5, v6)]:
                    v1 |= 1
                    break
        return v1
