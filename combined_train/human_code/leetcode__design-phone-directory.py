class C1(object):

    def __init__(self, a1):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.__curr = 0
        self.__numbers = list(range(a1))
        self.__used = [False] * a1

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.__curr == len(self.__numbers):
            return -1
        v1 = self.__numbers[self.__curr]
        self.__curr += 1
        self.__used[v1] = True
        return v1

    def check(self, a1):
        """
        Check if a number is available or not.
        """
        return 0 <= a1 < len(self.__numbers) and (not self.__used[a1])

    def release(self, a1):
        """
        Recycle or release a number.
        """
        if not 0 <= a1 < len(self.__numbers) or not self.__used[a1]:
            return
        self.__used[a1] = False
        self.__curr -= 1
        self.__numbers[self.__curr] = a1
