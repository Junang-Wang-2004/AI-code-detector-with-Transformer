class C1(object):

    def __init__(self):
        self.__books = []

    def book(self, a1, a2):
        """
        """
        v1 = bisect.bisect_left(self.__books, (a1, 1))
        if v1 < len(self.__books) and self.__books[v1][0] == a1:
            self.__books[v1] = (self.__books[v1][0], self.__books[v1][1] + 1)
        else:
            self.__books.insert(v1, (a1, 1))
        v2 = bisect.bisect_left(self.__books, (a2, 1))
        if v2 < len(self.__books) and self.__books[v2][0] == a2:
            self.__books[v2] = (self.__books[v2][0], self.__books[v2][1] - 1)
        else:
            self.__books.insert(v2, (a2, -1))
        v3, v4 = (0, 0)
        for v5 in self.__books:
            v4 += v5[1]
            v3 = max(v3, v4)
        return v3
