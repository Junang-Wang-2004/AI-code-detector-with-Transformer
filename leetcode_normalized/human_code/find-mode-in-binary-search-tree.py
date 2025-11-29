class C1(object):

    def findMode(self, a1):
        """
        """

        def inorder(a1, a2, a3, a4, a5):
            if not a1:
                return (a2, a3, a4)
            a2, a3, a4 = inorder(a1.left, a2, a3, a4, a5)
            if a2:
                if a1.val == a2.val:
                    a3 += 1
                else:
                    a3 = 1
            if a3 > a4:
                a4 = a3
                del a5[:]
                a5.append(a1.val)
            elif a3 == a4:
                a5.append(a1.val)
            return inorder(a1.right, a1, a3, a4, a5)
        if not a1:
            return []
        v1 = []
        inorder(a1, None, 1, 0, v1)
        return v1
