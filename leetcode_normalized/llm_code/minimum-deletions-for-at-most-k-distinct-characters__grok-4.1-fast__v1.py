class C1(object):

    def minDeletion(self, a1, a2):
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = sorted((x for v4 in v1 if v4 > 0))
        v5 = len(v3)
        if v5 <= a2:
            return 0
        return sum(v3[:v5 - a2])
