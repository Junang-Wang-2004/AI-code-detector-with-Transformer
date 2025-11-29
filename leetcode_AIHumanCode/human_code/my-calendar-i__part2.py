# Time:  O(n^2)
# Space: O(n)
class MyCalendar2(object):

    def __init__(self):
        self.__calendar = []


    def book(self, start, end):
        """
        """
        for i, j in self.__calendar:
            if start < j and end > i:
                return False
        self.__calendar.append((start, end))
        return True



