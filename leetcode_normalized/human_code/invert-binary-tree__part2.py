class C1(object):

    def invertTree(self, a1):
        if a1 is not None:
            v1 = []
            v1.append(a1)
            while v1:
                v2 = v1.pop()
                v2.left, v2.right = (v2.right, v2.left)
                if v2.left is not None:
                    v1.append(v2.left)
                if v2.right is not None:
                    v1.append(v2.right)
        return a1
