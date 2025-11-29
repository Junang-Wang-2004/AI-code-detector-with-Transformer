class C1(object):

    def __init__(self):
        self.__accu = [1]

    def add(self, a1):
        """
        """
        if not a1:
            self.__accu = [1]
            return
        self.__accu.append(self.__accu[-1] * a1)

    def getProduct(self, a1):
        """
        """
        if len(self.__accu) <= a1:
            return 0
        return self.__accu[-1] // self.__accu[-1 - a1]
