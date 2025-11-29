# Time:  ctor:      O(1)
#        getRandom: O(n)
# Space: O(1)

from random import randint


# if the length is unknown without using extra space
class Solution(object):

    def __init__(self, head):
        """
        """
        self.__head = head


    # Proof of Reservoir Sampling:
    # https://discuss.leetcode.com/topic/53753/brief-explanation-for-reservoir-sampling
    def getRandom(self):
        """
        """
        reservoir = -1
        curr, n = self.__head, 0
        while curr:
            reservoir = curr.val if randint(1, n+1) == 1 else reservoir
            curr, n = curr.__next__, n+1
        return reservoir


