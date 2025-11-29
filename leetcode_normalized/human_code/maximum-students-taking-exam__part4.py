class C1(object):

    def maxStudents(self, a1):
        """
        """

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        v1 = {0: 0}
        for v2 in a1:
            v3 = sum((1 << c for v4, v5 in enumerate(v2) if v5 == '#'))
            v6 = {}
            for v7, v8 in v1.items():
                for v9 in range(1 << len(a1[0])):
                    if v9 & v3 or v9 & v7 << 1 or v9 & v7 >> 1 or v9 & v9 << 1 or v9 & v9 >> 1:
                        continue
                    v6[v9] = max(v6.get(v9, 0), v8 + popcount(v9))
            v1 = v6
        return max(v1.values()) if v1 else 0
