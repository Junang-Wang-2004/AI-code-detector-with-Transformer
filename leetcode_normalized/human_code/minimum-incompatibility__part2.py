class C1(object):

    def minimumIncompatibility(self, a1, a2):
        """
        """
        v1 = (len(a1) - 1) * (len(a1) // a2) + 1
        v2 = [1]
        for v3 in range(len(a1)):
            v2.append(v2[-1] << 1)

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1

        def find_candidates(a1, a2):
            v1 = v2[len(a1)] - 1
            v2 = len(a1) // a2
            v3 = [v1] * (v1 + 1)
            for v4 in range(v1 + 1):
                if popcount(v4) != v2:
                    continue
                v5 = 0
                v6, v7 = (0, v1)
                for v8 in range(len(a1)):
                    if v4 & v2[v8] == 0:
                        continue
                    if v5 & v2[a1[v8]]:
                        break
                    v5 |= v2[a1[v8]]
                    v6 = max(v6, a1[v8])
                    v7 = min(v7, a1[v8])
                else:
                    v3[v4] = v6 - v7
            return v3
        v4 = find_candidates(a1, a2)
        v5 = len(a1) // a2
        v6 = v2[len(a1)] - 1
        v7 = [v1] * (v6 + 1)
        v7[0] = 0
        for v8 in range(v6 + 1):
            if popcount(v8) % v5 != 0:
                continue
            v9 = v8
            while v9:
                v7[v8] = min(v7[v8], v7[v8 - v9] + v4[v9])
                v9 = v9 - 1 & v8
        return v7[-1] if v7[-1] != v1 else -1
