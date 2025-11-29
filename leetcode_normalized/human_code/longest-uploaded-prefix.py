class C1(object):

    def __init__(self, a1):
        """
        """
        self.__lookup = set()
        self.__curr = 0

    def upload(self, a1):
        """
        """
        self.__lookup.add(a1 - 1)
        while self.__curr in self.__lookup:
            self.__lookup.remove(self.__curr)
            self.__curr += 1

    def longest(self):
        """
        """
        return self.__curr
