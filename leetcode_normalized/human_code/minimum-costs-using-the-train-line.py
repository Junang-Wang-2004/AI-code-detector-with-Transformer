import itertools

class C1(object):

    def minimumCosts(self, a1, a2, a3):
        """
        """
        v1 = []
        v2 = [0, a3]
        for v3, v4 in zip(a1, a2):
            v2 = [min(v2[0] + v3, v2[1] + v4), min(v2[0] + (v3 + a3), v2[1] + v4)]
            v1.append(min(v2[0], v2[1]))
        return v1
