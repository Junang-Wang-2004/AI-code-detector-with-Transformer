import itertools

class C1(object):

    def canConvertString(self, a1, a2, a3):
        """
        """
        if len(a1) != len(a2):
            return False
        v1 = [0] * 26
        for v2, v3 in zip(a1, a2):
            v4 = (ord(v3) - ord(v2)) % len(v1)
            if v4 != 0 and v1[v4] * len(v1) + v4 > a3:
                return False
            v1[v4] += 1
        return True
