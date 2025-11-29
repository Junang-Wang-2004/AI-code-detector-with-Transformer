class C1(object):

    def solve(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = {}
        v3 = []
        for v4, v5 in a2:
            if v5 * v5 > len(a1):
                v6 = 0
                for v7 in range(v4, len(a1), v5):
                    v6 += a1[v7]
                    v6 %= v1
                v3.append(v6)
            else:
                v8 = v4 % v5
                if (v8, v5) not in v2:
                    v2[v8, v5] = [0]
                    for v7 in range(v8, len(a1), v5):
                        v2[v8, v5].append((v2[v8, v5][-1] + a1[v7]) % v1)
                v3.append((v2[v8, v5][-1] - v2[v8, v5][v4 // v5]) % v1)
        return v3
