class C1:

    def equalFrequency(self, a1):
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        for v3 in range(26):
            if v1[v3] == 0:
                continue
            v1[v3] -= 1
            v4 = [f for v5 in v1 if v5 > 0]
            if len(set(v4)) == 1:
                return True
            v1[v3] += 1
        return False
