import itertools

class C1(object):

    def numberOfSpecialChars(self, a1):
        """
        """
        v1 = [len(a1)] * 26
        v2 = [-1] * 26
        for v3, v4 in enumerate(a1):
            if v4.islower():
                v1[ord(v4) - ord('a')] = v3
            elif v2[ord(v4) - ord('A')] == -1:
                v2[ord(v4) - ord('A')] = v3
        return sum((v4 < y for v4, v5 in zip(v1, v2)))
