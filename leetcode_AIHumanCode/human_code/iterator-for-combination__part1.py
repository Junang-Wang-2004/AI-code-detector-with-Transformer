# Time:  O(k), per operation
# Space: O(k)

import itertools


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        """
        self.__it = itertools.combinations(characters, combinationLength)
        self.__curr = None
        self.__last = characters[-combinationLength:]

    def __next__(self):
        """
        """
        self.__curr = "".join(next(self.__it))
        return self.__curr
    
    def hasNext(self):
        """
        """
        return self.__curr != self.__last


