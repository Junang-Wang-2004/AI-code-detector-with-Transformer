import itertools

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def leafSimilar(self, a1, a2):
        """
        """

        def dfs(a1):
            if not a1:
                return
            if not a1.left and (not a1.right):
                yield a1.val
            for v1 in dfs(a1.left):
                yield v1
            for v1 in dfs(a1.right):
                yield v1
        return all((a == b for v1, v2 in itertools.zip_longest(dfs(a1), dfs(a2))))
