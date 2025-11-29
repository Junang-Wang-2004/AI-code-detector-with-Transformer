from sortedcontainers import SortedList

class C1(object):

    def __init__(self):
        self.__sl = SortedList()
        self.__cnt = 0

    def add(self, a1, a2):
        """
        """
        v1 = self.__sl.bisect_right((a1,))
        if v1 - 1 >= 0 and self.__sl[v1 - 1][1] + 1 >= a1:
            v1 -= 1
            a1 = self.__sl[v1][0]
        v3 = []
        for v1 in range(v1, len(self.__sl)):
            if not a2 + 1 >= self.__sl[v1][0]:
                break
            a2 = max(a2, self.__sl[v1][1])
            self.__cnt -= self.__sl[v1][1] - self.__sl[v1][0] + 1
            v3.append(v1)
        while v3:
            del self.__sl[v3.pop()]
        self.__sl.add((a1, a2))
        self.__cnt += a2 - a1 + 1

    def count(self):
        """
        """
        return self.__cnt
