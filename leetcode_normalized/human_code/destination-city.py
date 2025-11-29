import itertools

class C1(object):

    def destCity(self, a1):
        """
        """
        v1, v2 = list(map(set, zip(*a1)))
        return (v2 - v1).pop()
