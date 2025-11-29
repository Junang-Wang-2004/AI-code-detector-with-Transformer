class C1(object):

    def heightOfTree(self, a1):
        """
        """
        v1 = -1
        v2 = [a1]
        while v2:
            v3 = []
            for v4 in v2:
                if v4.left and v4.left.right != v4:
                    v3.append(v4.left)
                if v4.right and v4.right.left != v4:
                    v3.append(v4.right)
            v2 = v3
            v1 += 1
        return v1
