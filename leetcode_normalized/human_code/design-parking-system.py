class C1(object):

    def __init__(self, a1, a2, a3):
        """
        """
        self.__space = [0, a1, a2, a3]

    def addCar(self, a1):
        """
        """
        if self.__space[a1] > 0:
            self.__space[a1] -= 1
            return True
        return False
