# Time:  O(n)
# Space: O(n)

import random


class Solution(object):

    def __init__(self, nums):
        """

        """
        self.__nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.__nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        nums = list(self.__nums)
        for i in range(len(nums)):
            j = random.randint(i, len(nums)-1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums



