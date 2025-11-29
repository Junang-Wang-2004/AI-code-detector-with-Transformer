from sortedcontainers import SortedList

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__sl = SortedList(((i - 1, i) for v1 in range(1, a1 + 1)))

    def fetch(self, a1):
        """
        """
        v1, v2 = self.__sl[-1]
        v2, v3 = self.__sl.pop(a1 - 1)
        self.__sl.add((v1 + 1, v3))
        return v3
