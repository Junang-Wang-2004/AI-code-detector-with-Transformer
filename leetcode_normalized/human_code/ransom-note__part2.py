import collections

class C1(object):

    def canConstruct(self, a1, a2):
        """
        """
        return not collections.Counter(a1) - collections.Counter(a2)
