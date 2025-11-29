# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        """
        if not nums:
            return
        self.__nums = nums
        self.__bit = [0] * (len(self.__nums) + 1)
        for i in range(1, len(self.__bit)):
            self.__bit[i] = nums[i-1] + self.__bit[i-1]

        for i in reversed(range(1, len(self.__bit))):
            last_i = i - (i & -i)
            self.__bit[i] -= self.__bit[last_i]

    def update(self, i, val):
        """
        """
        if val - self.__nums[i]:
            self.__add(i, val - self.__nums[i])
            self.__nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        """
        return self.__sum(j) - self.__sum(i-1)

    def __sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

    def __add(self, i, val):
        i += 1
        while i <= len(self.__nums):
            self.__bit[i] += val
            i += (i & -i)


