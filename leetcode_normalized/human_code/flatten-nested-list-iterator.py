class C1(object):

    def __init__(self, a1):
        """
        Initialize your data structure here.
        """
        self.__depth = [[a1, 0]]

    def __next__(self):
        """
        """
        v1, v2 = self.__depth[-1]
        self.__depth[-1][1] += 1
        return v1[v2].getInteger()

    def hasNext(self):
        """
        """
        while self.__depth:
            v1, v2 = self.__depth[-1]
            if v2 == len(v1):
                self.__depth.pop()
            elif v1[v2].isInteger():
                return True
            else:
                self.__depth[-1][1] += 1
                self.__depth.append([v1[v2].getList(), 0])
        return False
