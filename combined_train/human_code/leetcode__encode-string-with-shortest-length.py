class C1(object):

    def encode(self, a1):
        """
        """

        def encode_substr(a1, a2, a3, a4):
            v1 = a2[a3:a4 + 1]
            v2 = (v1 + v1).find(v1, 1)
            if v2 >= len(v1):
                return v1
            return str(len(v1) / v2) + '[' + a1[a3][a3 + v2 - 1] + ']'
        v1 = [['' for v2 in range(len(a1))] for v2 in range(len(a1))]
        for v3 in range(1, len(a1) + 1):
            for v4 in range(len(a1) + 1 - v3):
                v5 = v4 + v3 - 1
                v1[v4][v5] = a1[v4:v4 + v3]
                for v6 in range(v4, v5):
                    if len(v1[v4][v6]) + len(v1[v6 + 1][v5]) < len(v1[v4][v5]):
                        v1[v4][v5] = v1[v4][v6] + v1[v6 + 1][v5]
                v7 = encode_substr(v1, a1, v4, v5)
                if len(v7) < len(v1[v4][v5]):
                    v1[v4][v5] = v7
        return v1[0][len(a1) - 1]
