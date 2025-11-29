import random

class C1(object):

    def __init__(self, a1):
        """

        """
        self.__nums = a1

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.__nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        v1 = list(self.__nums)
        for v2 in range(len(v1)):
            v3 = random.randint(v2, len(v1) - 1)
            v1[v2], v1[v3] = (v1[v3], v1[v2])
        return v1
