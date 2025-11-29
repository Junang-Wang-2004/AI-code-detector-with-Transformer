import collections

class C1(object):

    def copyRandomBinaryTree(self, a1):
        """
        """
        v1 = collections.defaultdict(lambda: NodeCopy())
        v1[None] = None
        v2 = [a1]
        while v2:
            v3 = v2.pop()
            if not v3:
                continue
            v1[v3].val = v3.val
            v1[v3].left = v1[v3.left]
            v1[v3].right = v1[v3.right]
            v1[v3].random = v1[v3.random]
            v2.append(v3.right)
            v2.append(v3.left)
        return v1[a1]
