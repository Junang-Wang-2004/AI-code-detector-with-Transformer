import collections

class C1(object):

    def __init__(self):
        self.__left, self.__right = (collections.deque(), collections.deque())

    def pushFront(self, a1):
        """
        """
        self.__left.appendleft(a1)
        self.__balance()

    def pushMiddle(self, a1):
        """
        """
        if len(self.__left) > len(self.__right):
            self.__right.appendleft(self.__left.pop())
        self.__left.append(a1)

    def pushBack(self, a1):
        """
        """
        self.__right.append(a1)
        self.__balance()

    def popFront(self):
        """
        """
        v1 = (self.__left or collections.deque([-1])).popleft()
        self.__balance()
        return v1

    def popMiddle(self):
        """
        """
        v1 = (self.__left or [-1]).pop()
        self.__balance()
        return v1

    def popBack(self):
        """
        """
        v1 = (self.__right or self.__left or [-1]).pop()
        self.__balance()
        return v1

    def __balance(self):
        if len(self.__left) > len(self.__right) + 1:
            self.__right.appendleft(self.__left.pop())
        elif len(self.__left) < len(self.__right):
            self.__left.append(self.__right.popleft())
