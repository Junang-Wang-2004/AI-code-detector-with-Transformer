# Time:  O(nlogn) ~ O(n^2)
# Space: O(n)

import bisect


class MyCalendarThree(object):

    def __init__(self):
        self.__books = [[-1, 0]]
        self.__count = 0

    def book(self, start, end):
        """
        """
        i = bisect.bisect_right(self.__books, [start, float("inf")])
        if self.__books[i-1][0] == start:
            i -= 1
        else:
            self.__books.insert(i, [start, self.__books[i-1][1]])
        j = bisect.bisect_right(self.__books, [end, float("inf")])
        if self.__books[j-1][0] == end:
            j -= 1
        else:
            self.__books.insert(j, [end, self.__books[j-1][1]])            
        for k in range(i, j):
            self.__books[k][1] += 1
            self.__count = max(self.__count, self.__books[k][1])
        return self.__count


