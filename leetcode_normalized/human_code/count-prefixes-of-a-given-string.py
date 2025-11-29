import itertools

class C1(object):

    def countPrefixes(self, a1, a2):
        """
        """
        return sum(map(a2.startswith, a1))
