import bisect

class C1(object):

    def __init__(self):
        v1 = 10 ** 5
        self.__lookup = [0]
        v2 = 10
        while v2 < v1:
            self.__lookup.append(v2)
            v2 *= 10
        self.__lookup.append(v2)

    def findNumbers(self, a1):
        """
        """

        def digit_count(a1):
            return bisect.bisect_right(self.__lookup, a1)
        return sum((digit_count(n) % 2 == 0 for v1 in a1))
