class C1(object):

    def __init__(self, a1):
        """
        """
        self.__rectangle = a1
        self.__updates = []

    def updateSubrectangle(self, a1, a2, a3, a4, a5):
        """
        """
        self.__updates.append((a1, a2, a3, a4, a5))

    def getValue(self, a1, a2):
        """
        """
        for v1, v2, v3, v4, v5 in reversed(self.__updates):
            if v1 <= a1 <= v3 and v2 <= a2 <= v4:
                return v5
        return self.__rectangle[a1][a2]
