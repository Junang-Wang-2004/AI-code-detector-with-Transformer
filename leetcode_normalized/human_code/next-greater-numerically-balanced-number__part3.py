import itertools

class C1(object):

    def nextBeautifulNumber(self, a1):
        """
        """
        v1 = [1, 22, 122, 333, 1333, 4444, 14444, 22333, 55555, 122333, 155555, 224444, 666666]
        v2 = tuple(str(a1))
        v3 = 1224444
        for v4 in v1:
            v4 = tuple(str(v4))
            if len(v4) < len(v2):
                continue
            if len(v4) > len(v2):
                v3 = min(v3, int(''.join(v4)))
                continue
            for v5 in itertools.permutations(v4):
                if v5 > v2:
                    v3 = min(v3, int(''.join(v5)))
        return v3
