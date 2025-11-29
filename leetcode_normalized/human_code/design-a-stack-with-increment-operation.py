class C1(object):

    def __init__(self, a1):
        """
        """
        self.__max_size = a1
        self.__stk = []

    def push(self, a1):
        """
        """
        if len(self.__stk) == self.__max_size:
            return
        self.__stk.append([a1, 0])

    def pop(self):
        """
        """
        if not self.__stk:
            return -1
        v1, v2 = self.__stk.pop()
        if self.__stk:
            self.__stk[-1][1] += v2
        return v1 + v2

    def increment(self, a1, a2):
        """
        """
        v1 = min(len(self.__stk), a1) - 1
        if v1 >= 0:
            self.__stk[v1][1] += a2
