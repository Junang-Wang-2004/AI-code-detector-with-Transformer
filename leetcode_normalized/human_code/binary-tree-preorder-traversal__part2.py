class C1(object):

    def preorderTraversal(self, a1):
        """
        """
        v1, v2 = ([], [(a1, False)])
        while v2:
            a1, v4 = v2.pop()
            if a1 is None:
                continue
            if v4:
                v1.append(a1.val)
            else:
                v2.append((a1.right, False))
                v2.append((a1.left, False))
                v2.append((a1, True))
        return v1
