class C1(object):

    def rightSideView(self, a1):
        if a1 is None:
            return []
        v1, v2 = ([], [a1])
        while v2:
            v3 = []
            for v4 in v2:
                if v4.left:
                    v3.append(v4.left)
                if v4.right:
                    v3.append(v4.right)
            v1.append(v4.val)
            v2 = v3
        return v1
