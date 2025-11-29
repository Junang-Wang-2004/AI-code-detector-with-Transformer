class C1(object):

    def minAbbreviation(self, a1, a2):
        """
        """

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
        v5 = a1
        for v6 in range(2 ** len(a1)):
            v7 = bits_to_abbr(a1, v6)
            if all((d & v6 for v8 in v1)) and len(v7) < len(v5):
                v5 = v7
        return v5
