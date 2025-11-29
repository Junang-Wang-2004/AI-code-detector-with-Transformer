import collections

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__lookup = collections.defaultdict(int)

    def setCell(self, a1, a2):
        """
        """
        self.__lookup[a1] = a2

    def resetCell(self, a1):
        """
        """
        if a1 in self.__lookup:
            del self.__lookup[a1]

    def getValue(self, a1):
        """
        """
        v1, v2 = a1[1:].split('+')
        v3 = self.__lookup.get(v1, 0) if v1[0].isalpha() else int(v1)
        v4 = self.__lookup.get(v2, 0) if v2[0].isalpha() else int(v2)
        return v3 + v4
