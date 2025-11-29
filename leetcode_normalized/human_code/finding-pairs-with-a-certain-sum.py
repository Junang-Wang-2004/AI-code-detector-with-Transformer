import collections

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__nums2 = a2
        self.__count1 = collections.Counter(a1)
        self.__count2 = collections.Counter(a2)

    def add(self, a1, a2):
        """
        """
        self.__count2[self.__nums2[a1]] -= 1
        self.__nums2[a1] += a2
        self.__count2[self.__nums2[a1]] += 1

    def count(self, a1):
        """
        """
        return sum((cnt * self.__count2[a1 - x] for v1, v2 in self.__count1.items()))
