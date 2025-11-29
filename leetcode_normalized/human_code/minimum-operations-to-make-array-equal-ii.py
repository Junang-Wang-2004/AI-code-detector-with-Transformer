import itertools

class C1(object):

    def minOperations(self, a1, a2, a3):
        """
        """
        v1 = v2 = 0
        for v3, v4 in zip(a1, a2):
            if v4 == v3:
                continue
            if a3 == 0 or (v4 - v3) % a3:
                return -1
            if v3 < v4:
                v1 += (v4 - v3) // a3
            else:
                v2 += (v3 - v4) // a3
        return v1 if v1 == v2 else -1
