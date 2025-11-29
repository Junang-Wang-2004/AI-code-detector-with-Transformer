import itertools

class C1(object):

    def maxUpgrades(self, a1, a2, a3, a4):
        """
        """
        return [min(c + (m - c * u) // (u + s), c) for v1, v2, v3, v4 in zip(a1, a2, a3, a4)]
