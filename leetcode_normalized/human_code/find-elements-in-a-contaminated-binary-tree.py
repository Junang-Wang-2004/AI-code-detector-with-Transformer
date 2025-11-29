class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def __init__(self, a1):
        """
        """

        def dfs(a1, a2, a3):
            if not a1:
                return
            a1.val = a2
            a3.add(a2)
            dfs(a1.left, 2 * a2 + 1, a3)
            dfs(a1.right, 2 * a2 + 2, a3)
        self.__lookup = set()
        dfs(a1, 0, self.__lookup)

    def find(self, a1):
        """
        """
        return a1 in self.__lookup
