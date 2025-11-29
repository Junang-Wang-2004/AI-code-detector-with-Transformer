import collections

class C1(object):

    def subtreeWithAllDeepest(self, a1):
        """
        """
        v1 = collections.namedtuple('Result', ('node', 'depth'))

        def dfs(a1):
            if not a1:
                return v1(None, 0)
            v1, v2 = (dfs(a1.left), dfs(a1.right))
            if v1.depth > v2.depth:
                return v1(v1.node, v1.depth + 1)
            if v1.depth < v2.depth:
                return v1(v2.node, v2.depth + 1)
            return v1(a1, v1.depth + 1)
        return dfs(a1).node
