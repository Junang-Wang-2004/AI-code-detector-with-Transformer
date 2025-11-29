from random import randint
from collections import defaultdict

class C1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__list = []
        self.__used = defaultdict(list)

    def insert(self, a1):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        v1 = a1 in self.__used
        self.__list += ((a1, len(self.__used[a1])),)
        self.__used[a1] += (len(self.__list) - 1,)
        return not v1

    def remove(self, a1):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if a1 not in self.__used:
            return False
        self.__used[self.__list[-1][0]][self.__list[-1][1]] = self.__used[a1][-1]
        self.__list[self.__used[a1][-1]], self.__list[-1] = (self.__list[-1], self.__list[self.__used[a1][-1]])
        self.__used[a1].pop()
        if not self.__used[a1]:
            self.__used.pop(a1)
        self.__list.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        """
        return self.__list[randint(0, len(self.__list) - 1)][0]
