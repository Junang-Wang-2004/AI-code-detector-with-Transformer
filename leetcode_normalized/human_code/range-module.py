import bisect

class C1(object):

    def __init__(self):
        self.__intervals = []

    def addRange(self, a1, a2):
        """
        """
        v1 = []
        v2 = 0
        for v3 in self.__intervals:
            if a2 < v3[0]:
                v1.append((a1, a2))
                break
            elif v3[1] < a1:
                v1.append(v3)
            else:
                a1 = min(a1, v3[0])
                a2 = max(a2, v3[1])
            v2 += 1
        if v2 == len(self.__intervals):
            v1.append((a1, a2))
        while v2 < len(self.__intervals):
            v1.append(self.__intervals[v2])
            v2 += 1
        self.__intervals = v1

    def queryRange(self, a1, a2):
        """
        """
        v1 = bisect.bisect_left(self.__intervals, (a1, float('inf')))
        if v1:
            v1 -= 1
        return bool(self.__intervals) and self.__intervals[v1][0] <= a1 and (a2 <= self.__intervals[v1][1])

    def removeRange(self, a1, a2):
        """
        """
        v1 = []
        for v2 in self.__intervals:
            if v2[1] <= a1 or v2[0] >= a2:
                v1.append(v2)
            else:
                if v2[0] < a1:
                    v1.append((v2[0], a1))
                if a2 < v2[1]:
                    v1.append((a2, v2[1]))
        self.__intervals = v1
