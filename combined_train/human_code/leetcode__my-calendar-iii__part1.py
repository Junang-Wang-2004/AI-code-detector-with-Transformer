import bisect

class C1(object):

    def __init__(self):
        self.__books = [[-1, 0]]
        self.__count = 0

    def book(self, a1, a2):
        """
        """
        v1 = bisect.bisect_right(self.__books, [a1, float('inf')])
        if self.__books[v1 - 1][0] == a1:
            v1 -= 1
        else:
            self.__books.insert(v1, [a1, self.__books[v1 - 1][1]])
        v2 = bisect.bisect_right(self.__books, [a2, float('inf')])
        if self.__books[v2 - 1][0] == a2:
            v2 -= 1
        else:
            self.__books.insert(v2, [a2, self.__books[v2 - 1][1]])
        for v3 in range(v1, v2):
            self.__books[v3][1] += 1
            self.__count = max(self.__count, self.__books[v3][1])
        return self.__count
