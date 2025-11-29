# Time:  ctor: O(n)
#        pick: O(1)
# Space: O(n)

from random import randint
import collections


class Solution(object):

    def __init__(self, nums):
        """
        """
        self.__lookup = collections.defaultdict(list)
        for i, x in enumerate(nums):
            self.__lookup[x].append(i)

    def pick(self, target):
        """
        """
        return self.__lookup[target][randint(0, len(self.__lookup[target])-1)]


