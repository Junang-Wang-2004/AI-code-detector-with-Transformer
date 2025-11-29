import re

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__result = re.findall('([a-zA-Z])(\\d+)', a1)
        self.__index, self.__num, self.__ch = (0, 0, ' ')

    def __next__(self):
        """
        """
        if not self.hasNext():
            return ' '
        if self.__num == 0:
            self.__ch = self.__result[self.__index][0]
            self.__num = int(self.__result[self.__index][1])
            self.__index += 1
        self.__num -= 1
        return self.__ch

    def hasNext(self):
        """
        """
        return self.__index != len(self.__result) or self.__num != 0
