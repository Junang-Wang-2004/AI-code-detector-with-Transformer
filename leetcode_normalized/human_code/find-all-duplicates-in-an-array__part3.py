from collections import Counter

class C1(object):

    def findDuplicates(self, a1):
        """
        """
        return [elem for v1, v2 in list(Counter(a1).items()) if v2 == 2]
