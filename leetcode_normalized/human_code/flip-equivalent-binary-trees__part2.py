class C1(object):

    def flipEquiv(self, a1, a2):
        """
        """
        v1, v2 = ([a1], [a2])
        while v1 and v2:
            v3, v4 = (v1.pop(), v2.pop())
            if not v3 and (not v4):
                continue
            if not v3 or not v4 or v3.val != v4.val:
                return False
            if not v3.left and (not v4.right) or (v3.left and v4.right and (v3.left.val == v4.right.val)):
                v1.extend([v3.right, v3.left])
            else:
                v1.extend([v3.left, v3.right])
            v2.extend([v4.left, v4.right])
        return not v1 and (not v2)
