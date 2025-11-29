from random import randint

class C1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__set = []
        self.__used = {}

    def insert(self, a1):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if a1 in self.__used:
            return False
        self.__set += (a1,)
        self.__used[a1] = len(self.__set) - 1
        return True

    def remove(self, a1):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if a1 not in self.__used:
            return False
        self.__used[self.__set[-1]] = self.__used[a1]
        self.__set[self.__used[a1]], self.__set[-1] = (self.__set[-1], self.__set[self.__used[a1]])
        self.__used.pop(a1)
        self.__set.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return self.__set[randint(0, len(self.__set) - 1)]
