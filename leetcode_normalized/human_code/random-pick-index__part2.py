from random import randint

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__nums = a1

    def pick(self, a1):
        """
        """
        v1 = -1
        v2 = 0
        for v3 in range(len(self.__nums)):
            if self.__nums[v3] != a1:
                continue
            v1 = v3 if randint(1, v2 + 1) == 1 else v1
            v2 += 1
        return v1
