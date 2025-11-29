# Time:  ctor:      O(n)
#        getRandom: O(1)
# Space: O(n)
from random import randint


# if the length is known with using extra space
class Solution2(object):

    def __init__(self, head):
        """
        """
        self.__lookup = []
        while head:
            self.__lookup.append(head.val)
            head = head.__next__
        

    def getRandom(self):
        """
        """
        return self.__lookup[randint(0, len(self.__lookup)-1)]
