from random import randint

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__lookup = []
        while a1:
            self.__lookup.append(a1.val)
            a1 = a1.__next__

    def getRandom(self):
        """
        """
        return self.__lookup[randint(0, len(self.__lookup) - 1)]
