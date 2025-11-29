import itertools

class C1(object):

    def numberOfSpecialChars(self, a1):
        """
        """
        v1 = [False] * 26
        v2 = [False] * 26
        for v3 in a1:
            if v3.islower():
                v1[ord(v3) - ord('a')] = True
            else:
                v2[ord(v3) - ord('A')] = True
        return sum((v3 == y == True for v3, v4 in zip(v1, v2)))
