class C1:

    def lastNonEmptyString(self, a1):
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = max(v1)
        v4 = [False] * 26
        v5 = []
        for v6 in range(len(a1) - 1, -1, -1):
            v7 = ord(a1[v6]) - ord('a')
            if not v4[v7] and v1[v7] == v3:
                v5.append(a1[v6])
                v4[v7] = True
        return ''.join(v5[::-1])
