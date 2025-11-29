class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def __init__(self, a1):
        self.__stk = []
        self.__traversalLeft(a1)

    def hasNext(self):
        return self.__stk

    def __next__(self):
        v1 = self.__stk.pop()
        self.__traversalLeft(v1.right)
        return v1.val

    def __traversalLeft(self, a1):
        while a1 is not None:
            self.__stk.append(a1)
            a1 = a1.left
