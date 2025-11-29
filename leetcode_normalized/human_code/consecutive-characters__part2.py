import itertools

class C1(object):

    def maxPower(self, a1):
        return max((len(list(v)) for v1, v2 in itertools.groupby(a1)))
