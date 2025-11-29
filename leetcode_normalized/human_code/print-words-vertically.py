import itertools

class C1(object):

    def printVertically(self, a1):
        """
        """
        return [''.join(c).rstrip() for v1 in itertools.zip_longest(*a1.split(), fillvalue=' ')]
