class C1:

    def canMakeSubsequence(self, a1, a2):
        v1, v2 = (0, 0)
        while v1 < len(a1) and v2 < len(a2):
            if (ord(a2[v2]) - ord(a1[v1])) % 26 <= 1:
                v2 += 1
            v1 += 1
        return v2 == len(a2)
