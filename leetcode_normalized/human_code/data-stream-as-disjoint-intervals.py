class C1(object):

    def __init__(self, a1=0, a2=0):
        self.start = a1
        self.end = a2

class C2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__intervals = []

    def addNum(self, a1):
        """
        """

        def upper_bound(a1, a2):
            v1, v2 = (0, len(a1) - 1)
            while v1 <= v2:
                v3 = v1 + (v2 - v1) / 2
                if a1[v3].start > a2:
                    v2 = v3 - 1
                else:
                    v1 = v3 + 1
            return v1
        v1 = upper_bound(self.__intervals, a1)
        v2, v3 = (a1, a1)
        if v1 != 0 and self.__intervals[v1 - 1].end + 1 >= a1:
            v1 -= 1
        while v1 != len(self.__intervals) and v3 + 1 >= self.__intervals[v1].start:
            v2 = min(v2, self.__intervals[v1].start)
            v3 = max(v3, self.__intervals[v1].end)
            del self.__intervals[v1]
        self.__intervals.insert(v1, C1(v2, v3))

    def getIntervals(self):
        """
        """
        return self.__intervals
