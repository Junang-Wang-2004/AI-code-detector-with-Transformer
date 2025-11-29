class C1(object):

    def substringXorQueries(self, a1, a2):
        """
        """
        v1 = max((a ^ b for v2, v3 in a2))
        v4 = {}
        for v5 in range(len(a1)):
            v6 = 0
            for v7 in range(v5, len(a1)):
                v6 = (v6 << 1) + int(a1[v7])
                if v6 > v1:
                    break
                if v6 not in v4:
                    v4[v6] = [v5, v7]
                if a1[v5] == '0':
                    break
        return [v4[v2 ^ v3] if v2 ^ v3 in v4 else [-1, -1] for v2, v3 in a2]
