class C1:

    def closestValue(self, a1, a2):
        v1 = None
        v2 = None
        v3 = a1
        while v3:
            if v3.val <= a2:
                v1 = v3.val
                v3 = v3.right
            else:
                v3 = v3.left
        v3 = a1
        while v3:
            if v3.val >= a2:
                v2 = v3.val
                v3 = v3.left
            else:
                v3 = v3.right
        if v1 is None:
            return v2
        if v2 is None:
            return v1
        return v1 if abs(v1 - a2) <= abs(v2 - a2) else v2
