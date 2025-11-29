import collections

class C1(object):

    def singleNumber(self, a1):
        """
        """
        return list((collections.Counter(list(set(a1)) * 3) - collections.Counter(a1)).keys())[0]
