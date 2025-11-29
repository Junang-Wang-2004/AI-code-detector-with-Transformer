# Time:  ctor:        O(1)
#        record:      O(1)
#        totalScore: O(logn)
# Space: O(n)

import bisect


# prefix sum, binary search
class ExamTracker(object):

    def __init__(self):
        self.__times = []
        self.__prefix = [0]

    def record(self, time, score):
        """
        """
        self.__times.append(time)
        self.__prefix.append(self.__prefix[-1]+score)

    def totalScore(self, startTime, endTime):
        """
        """
        i = bisect.bisect_left(self.__times, startTime)
        j = bisect.bisect_right(self.__times, endTime)-1
        return self.__prefix[j+1]-self.__prefix[i]
