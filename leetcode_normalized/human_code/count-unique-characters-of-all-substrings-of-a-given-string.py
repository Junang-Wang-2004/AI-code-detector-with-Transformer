import string

class C1(object):

    def uniqueLetterString(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = {c: [-1, -1] for v3 in string.ascii_uppercase}
        v4 = 0
        for v5, v3 in enumerate(a1):
            v6, v7 = v2[v3]
            v4 = (v4 + (v5 - v7) * (v7 - v6)) % v1
            v2[v3] = [v7, v5]
        for v3 in v2:
            v6, v7 = v2[v3]
            v4 = (v4 + (len(a1) - v7) * (v7 - v6)) % v1
        return v4
