class C1:

    def groupAnagrams(self, a1):
        v1 = {}
        for v2 in a1:
            v3 = [0] * 26
            for v4 in v2:
                v3[ord(v4) - ord('a')] += 1
            v5 = tuple(v3)
            if v5 not in v1:
                v1[v5] = []
            v1[v5].append(v2)
        v6 = []
        for v7 in v1.values():
            v7.sort()
            v6.append(v7)
        return v6
