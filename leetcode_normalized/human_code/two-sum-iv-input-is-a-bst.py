class C1(object):

    def findTarget(self, a1, a2):
        """
        """

        class BSTIterator(object):

            def __init__(self, a1, a2):
                self.__node = a1
                self.__forward = a2
                self.__s = []
                self.__cur = None
                next(self)

            def val(self):
                return self.__cur

            def __next__(self):
                while self.__node or self.__s:
                    if self.__node:
                        self.__s.append(self.__node)
                        self.__node = self.__node.left if self.__forward else self.__node.right
                    else:
                        self.__node = self.__s.pop()
                        self.__cur = self.__node.val
                        self.__node = self.__node.right if self.__forward else self.__node.left
                        break
        if not a1:
            return False
        v1, v2 = (BSTIterator(a1, True), BSTIterator(a1, False))
        while v1.val() < v2.val():
            if v1.val() + v2.val() == a2:
                return True
            elif v1.val() + v2.val() < a2:
                next(v1)
            else:
                next(v2)
        return False
