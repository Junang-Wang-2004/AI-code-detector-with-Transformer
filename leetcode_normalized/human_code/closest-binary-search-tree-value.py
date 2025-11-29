class C1(object):

    def closestValue(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = float('inf')
        while a1:
            if abs(a1.val - a2) < v1:
                v1 = abs(a1.val - a2)
                v2 = a1.val
            if a2 == a1.val:
                break
            elif a2 < a1.val:
                a1 = a1.left
            else:
                a1 = a1.right
        return v2
