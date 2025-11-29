import collections

class C1(object):

    def removeAnagrams(self, a1):
        """
        """
        return [a1[i] for v1 in range(len(a1)) if v1 == 0 or sorted(a1[v1 - 1]) != sorted(a1[v1])]
