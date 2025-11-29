class C1:

    def isItPossible(self, a1, a2):
        v1 = [0] * 26
        v2 = [0] * 26
        for v3 in a1:
            v1[ord(v3) - ord('a')] += 1
        for v3 in a2:
            v2[ord(v3) - ord('a')] += 1
        v4 = sum((1 for v5 in v1 if v5 > 0))
        v6 = sum((1 for v5 in v2 if v5 > 0))
        v7 = any((v1[i] > 0 and v2[i] > 0 for v8 in range(26)))
        if v4 == v6 and v7:
            return True
        for v8 in range(26):
            if v1[v8] == 0:
                continue
            for v9 in range(26):
                if v2[v9] == 0 or v8 == v9:
                    continue
                v10 = v4 - (1 if v1[v8] == 1 else 0) + (1 if v1[v9] == 0 else 0)
                v11 = v6 - (1 if v2[v9] == 1 else 0) + (1 if v2[v8] == 0 else 0)
                if v10 == v11:
                    return True
        return False
