class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def smallestFromLeaf(self, a1):
        """
        """

        def dfs(a1, a2, a3):
            if not a1:
                return
            a2.append(chr(ord('a') + a1.val))
            if not a1.left and (not a1.right):
                a3[0] = min(a3[0], ''.join(reversed(a2)))
            dfs(a1.left, a2, a3)
            dfs(a1.right, a2, a3)
            a2.pop()
        v1 = ['~']
        dfs(a1, [], v1)
        return v1[0]
