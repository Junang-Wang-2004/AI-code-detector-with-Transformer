import collections

class C1(object):

    def singleNumber(self, a1):
        """
        """
        return (sum(set(a1)) * 3 - sum(a1)) / 2
