class C1(object):

    def __init__(self):
        self.__lookup = {'': -1}

    def create(self, a1, a2):
        """
        """
        if a1[:a1.rfind('/')] not in self.__lookup:
            return False
        self.__lookup[a1] = a2
        return True

    def get(self, a1):
        """
        """
        if a1 not in self.__lookup:
            return -1
        return self.__lookup[a1]
