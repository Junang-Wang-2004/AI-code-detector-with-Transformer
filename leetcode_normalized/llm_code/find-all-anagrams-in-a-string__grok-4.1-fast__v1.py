class C1(object):

    def findAnagrams(self, a1, a2):
        if not a2 or len(a2) > len(a1):
            return []
        v1 = []
        v2 = [0] * 26
        for v3 in a2:
            v2[ord(v3) - ord('a')] += 1
        v4 = [0] * 26
        v5 = len(a2)
        for v6 in range(v5):
            v4[ord(a1[v6]) - ord('a')] += 1
        if v4 == v2:
            v1.append(0)
        for v6 in range(v5, len(a1)):
            v4[ord(a1[v6 - v5]) - ord('a')] -= 1
            v4[ord(a1[v6]) - ord('a')] += 1
            if v4 == v2:
                v1.append(v6 - v5 + 1)
        return v1
