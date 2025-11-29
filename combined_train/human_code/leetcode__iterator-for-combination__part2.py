import functools

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__characters = a1
        self.__combinationLength = a2
        self.__it = self.__iterative_backtracking()
        self.__curr = None
        self.__last = a1[-a2:]

    def __iterative_backtracking(self):

        def conquer():
            if len(curr) == self.__combinationLength:
                return curr

        def prev_divide(a1):
            curr.append(a1)

        def divide(a1):
            if len(curr) != self.__combinationLength:
                for v1 in reversed(range(a1, len(self.__characters) - (self.__combinationLength - len(curr) - 1))):
                    stk.append(functools.partial(post_divide))
                    stk.append(functools.partial(divide, v1 + 1))
                    stk.append(functools.partial(prev_divide, self.__characters[v1]))
            stk.append(functools.partial(conquer))

        def post_divide():
            curr.pop()
        v1 = []
        v2 = [functools.partial(divide, 0)]
        while v2:
            v3 = v2.pop()()
            if v3 is not None:
                yield v3

    def __next__(self):
        """
        """
        self.__curr = ''.join(next(self.__it))
        return self.__curr

    def hasNext(self):
        """
        """
        return self.__curr != self.__last
