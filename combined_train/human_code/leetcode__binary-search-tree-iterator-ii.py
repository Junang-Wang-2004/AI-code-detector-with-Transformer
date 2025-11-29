class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def __init__(self, a1):
        """
        """
        self.__stk = []
        self.__traversalLeft(a1)
        self.__vals = []
        self.__pos = -1

    def hasNext(self):
        """
        """
        return self.__pos + 1 != len(self.__vals) or self.__stk

    def __next__(self):
        """
        """
        self.__pos += 1
        if self.__pos == len(self.__vals):
            v1 = self.__stk.pop()
            self.__traversalLeft(v1.right)
            self.__vals.append(v1.val)
        return self.__vals[self.__pos]

    def hasPrev(self):
        """
        """
        return self.__pos - 1 >= 0

    def prev(self):
        """
        """
        self.__pos -= 1
        return self.__vals[self.__pos]

    def __traversalLeft(self, a1):
        while a1 is not None:
            self.__stk.append(a1)
            a1 = a1.left
