import math

class C1(object):

    def __init__(self):
        self.__max_log3 = int(math.log(2147483647) / math.log(3))
        self.__max_pow3 = 3 ** self.__max_log3

    def isPowerOfThree(self, a1):
        """
        """
        return a1 > 0 and self.__max_pow3 % a1 == 0
