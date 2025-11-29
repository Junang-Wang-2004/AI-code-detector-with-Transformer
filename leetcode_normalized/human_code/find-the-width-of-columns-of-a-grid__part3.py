import itertools

class C1(object):

    def findColumnWidth(self, a1):
        """
        """
        return [max((len(str(x)) for v1 in col)) for v2 in zip(*a1)]
