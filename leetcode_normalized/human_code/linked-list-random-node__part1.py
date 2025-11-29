from random import randint

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__head = a1

    def getRandom(self):
        """
        """
        v1 = -1
        v2, v3 = (self.__head, 0)
        while v2:
            v1 = v2.val if randint(1, v3 + 1) == 1 else v1
            v2, v3 = (v2.__next__, v3 + 1)
        return v1
