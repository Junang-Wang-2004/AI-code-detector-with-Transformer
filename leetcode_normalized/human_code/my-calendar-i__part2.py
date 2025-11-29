class C1(object):

    def __init__(self):
        self.__calendar = []

    def book(self, a1, a2):
        """
        """
        for v1, v2 in self.__calendar:
            if a1 < v2 and a2 > v1:
                return False
        self.__calendar.append((a1, a2))
        return True
