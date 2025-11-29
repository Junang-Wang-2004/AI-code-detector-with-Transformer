class C1(object):

    def __init__(self, a1):
        """
        initialize your data structure here.
        """
        if not a1:
            return
        self.__nums = a1
        self.__bit = [0] * (len(self.__nums) + 1)
        for v1 in range(1, len(self.__bit)):
            self.__bit[v1] = a1[v1 - 1] + self.__bit[v1 - 1]
        for v1 in reversed(range(1, len(self.__bit))):
            v2 = v1 - (v1 & -v1)
            self.__bit[v1] -= self.__bit[v2]

    def update(self, a1, a2):
        """
        """
        if a2 - self.__nums[a1]:
            self.__add(a1, a2 - self.__nums[a1])
            self.__nums[a1] = a2

    def sumRange(self, a1, a2):
        """
        sum of elements nums[i..j], inclusive.
        """
        return self.__sum(a2) - self.__sum(a1 - 1)

    def __sum(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 += self.__bit[a1]
            a1 -= a1 & -a1
        return v2

    def __add(self, a1, a2):
        a1 += 1
        while a1 <= len(self.__nums):
            self.__bit[a1] += a2
            a1 += a1 & -a1
