import itertools

class C1(object):

    def makeSimilar(self, a1, a2):
        """
        """
        a1.sort(key=lambda x: (x % 2, x))
        a2.sort(key=lambda x: (x % 2, x))
        return sum((abs(x - y) // 2 for v1, v2 in zip(a1, a2))) // 2
