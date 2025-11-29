from itertools import zip_longest

class C1(object):

    def addBinary(self, a1, a2):
        """
        """
        v1 = ''
        v2 = 0
        for v3, v4 in zip_longest(reversed(a1), reversed(a2), fillvalue='0'):
            v2, v5 = divmod(int(v3) + int(v4) + v2, 2)
            v1 += str(v5)
        if v2:
            v1 += str(v2)
        return v1[::-1]
