class C1(object):

    def minAbbreviation(self, a1, a2):
        """
        """

        def bits_to_abbr_len(a1, a2):
            v1 = 0
            v2 = 0
            for v3 in range(len(a1)):
                if a2 & 1:
                    if v3 - v2 > 0:
                        v1 += len(str(v3 - v2))
                    v2 = v3 + 1
                    v1 += 1
                elif v3 == len(a1) - 1:
                    v1 += len(str(v3 - v2 + 1))
                a2 >>= 1
            return v1

        def bits_to_abbr(a1, a2):
            v1 = []
            v2 = 0
            for v3 in range(len(a1)):
                if a2 & 1:
                    if v3 - v2 > 0:
                        v1.append(str(v3 - v2))
                    v2 = v3 + 1
                    v1.append(a1[v3])
                elif v3 == len(a1) - 1:
                    v1.append(str(v3 - v2 + 1))
                a2 >>= 1
            return ''.join(v1)
        v1 = []
        for v2 in a2:
            if len(v2) != len(a1):
                continue
            v1.append(sum((2 ** i for v3, v4 in enumerate(v2) if a1[v3] != v4)))
        if not v1:
            return str(len(a1))
        v5 = 2 ** len(a1) - 1
        for v6 in range(2 ** len(a1)):
            if all((d & v6 for v7 in v1)) and bits_to_abbr_len(a1, v6) < bits_to_abbr_len(a1, v5):
                v5 = v6
        return bits_to_abbr(a1, v5)
