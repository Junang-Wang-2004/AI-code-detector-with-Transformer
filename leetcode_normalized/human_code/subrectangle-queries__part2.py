class C1(object):

    def __init__(self, a1):
        """
        """
        self.__rectangle = a1

    def updateSubrectangle(self, a1, a2, a3, a4, a5):
        """
        """
        for v1 in range(a1, a3 + 1):
            for v2 in range(a2, a4 + 1):
                self.__rectangle[v1][v2] = a5

    def getValue(self, a1, a2):
        """
        """
        return self.__rectangle[a1][a2]
