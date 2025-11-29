from functools import reduce

class C1(object):

    def sumDistance(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        for v2 in range(len(a1)):
            a1[v2] += a3 if a2[v2] == 'R' else -a3
        a1.sort()
        return reduce(lambda x, y: (x + y) % v1, ((v2 - (len(a1) - (v2 + 1))) * x for v2, v3 in enumerate(a1)))
