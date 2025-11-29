class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def __init__(self, a1):
        """
        """
        self.__tree = [a1]
        for v1 in self.__tree:
            if v1.left:
                self.__tree.append(v1.left)
            if v1.right:
                self.__tree.append(v1.right)

    def insert(self, a1):
        """
        """
        v1 = len(self.__tree)
        self.__tree.append(C1(a1))
        if v1 % 2:
            self.__tree[(v1 - 1) // 2].left = self.__tree[-1]
        else:
            self.__tree[(v1 - 1) // 2].right = self.__tree[-1]
        return self.__tree[(v1 - 1) // 2].val

    def get_root(self):
        """
        """
        return self.__tree[0]
