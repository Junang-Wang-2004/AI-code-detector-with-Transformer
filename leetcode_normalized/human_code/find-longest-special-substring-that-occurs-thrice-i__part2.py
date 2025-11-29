class C1(object):

    def maximumLength(self, a1):
        """
        """
        v1 = [[0] for v2 in range(26)]
        v3 = 0
        for v4, v5 in enumerate(a1):
            v6 = v1[ord(v5) - ord('a')]
            for v7 in range(v4, len(a1)):
                if a1[v7] != a1[v4]:
                    break
                if v7 - v4 + 1 == len(v6):
                    v6.append(0)
                v6[v7 - v4 + 1] += 1
                if v6[v7 - v4 + 1] == 3:
                    v3 = max(v3, v7 - v4 + 1)
        return v3 if v3 else -1
