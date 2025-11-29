from sortedcontainers import SortedList

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__lookup = {}
        self.__sl = SortedList()
        for v1, v2, v3 in a1:
            self.add(v1, v2, v3)

    def add(self, a1, a2, a3):
        """
        """
        self.__sl.add((a3, a2, a1))
        self.__lookup[a2] = (a1, a3)

    def edit(self, a1, a2):
        """
        """
        v1, v2 = self.__lookup[a1]
        self.rmv(a1)
        self.add(v1, a1, a2)

    def rmv(self, a1):
        """
        """
        v1, v2 = self.__lookup.pop(a1)
        self.__sl.remove((v2, a1, v1))

    def execTop(self):
        """
        """
        if not self.__sl:
            return -1
        v1, v2, v3 = self.__sl[-1]
        self.rmv(v2)
        return v3
