class C1(object):

    def __init__(self, a1):
        """
        """
        self.__history = [a1]
        self.__curr = 0

    def visit(self, a1):
        """
        """
        while len(self.__history) > self.__curr + 1:
            self.__history.pop()
        self.__history.append(a1)
        self.__curr += 1

    def back(self, a1):
        """
        """
        self.__curr = max(self.__curr - a1, 0)
        return self.__history[self.__curr]

    def forward(self, a1):
        """
        """
        self.__curr = min(self.__curr + a1, len(self.__history) - 1)
        return self.__history[self.__curr]
