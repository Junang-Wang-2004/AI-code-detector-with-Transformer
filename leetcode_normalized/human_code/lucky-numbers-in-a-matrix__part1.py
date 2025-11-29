import itertools

class C1(object):

    def luckyNumbers(self, a1):
        """
        """
        v1 = list(map(min, a1))
        v2 = list(map(max, zip(*a1)))
        return [cell for v3, v4 in enumerate(a1) for v5, v6 in enumerate(v4) if v1[v3] == v2[v5]]
