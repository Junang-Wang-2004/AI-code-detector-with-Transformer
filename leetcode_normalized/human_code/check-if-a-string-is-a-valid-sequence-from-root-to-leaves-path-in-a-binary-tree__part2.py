class C1(object):

    def isValidSequence(self, a1, a2):
        """
        """
        v1 = [(a1, 0)]
        while v1:
            v2, v3 = v1.pop()
            if not v2 or v3 == len(a2) or v2.val != a2[v3]:
                continue
            if v3 + 1 == len(a2) and v2.left == v2.right:
                return True
            v1.append((v2.right, v3 + 1))
            v1.append((v2.left, v3 + 1))
        return False
