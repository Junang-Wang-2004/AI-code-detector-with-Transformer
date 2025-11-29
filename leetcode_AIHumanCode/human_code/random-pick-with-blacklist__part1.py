# Time:  ctor: O(b)
#        pick: O(1)
# Space: O(b)

import random


class Solution(object):
    
    def __init__(self, N, blacklist):
        """
        """
        self.__n = N-len(blacklist)
        self.__lookup = {}
        white = iter(set(range(self.__n, N))-set(blacklist))
        for black in blacklist:
            if black < self.__n:
                self.__lookup[black] = next(white)
        
        
    def pick(self):
        """
        """
        index = random.randint(0, self.__n-1)
        return self.__lookup[index] if index in self.__lookup else index


