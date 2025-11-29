class C1(object):

    def __init__(self):
        self.__overlaps = []
        self.__calendar = []

    def book(self, a1, a2):
        """
        """
        for v1, v2 in self.__overlaps:
            if a1 < v2 and a2 > v1:
                return False
        for v1, v2 in self.__calendar:
            if a1 < v2 and a2 > v1:
                self.__overlaps.append((max(a1, v1), min(a2, v2)))
        self.__calendar.append((a1, a2))
        return True
