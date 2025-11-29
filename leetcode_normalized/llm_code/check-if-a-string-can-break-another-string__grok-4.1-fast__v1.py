class C1:

    def checkIfCanBreak(self, a1, a2):

        def dominates(a1, a2):
            v1 = [0] * 26
            v2 = [0] * 26
            for v3 in a1:
                v1[ord(v3) - ord('a')] += 1
            for v3 in a2:
                v2[ord(v3) - ord('a')] += 1
            v4, v5 = (0, 0)
            for v6 in range(26):
                v4 += v1[v6]
                v5 += v2[v6]
                if v4 < v5:
                    return False
            return True
        return dominates(a1, a2) or dominates(a2, a1)
