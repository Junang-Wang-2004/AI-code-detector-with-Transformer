class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def flipMatchVoyage(self, a1, a2):
        v1 = []

        def traverse(a1, a2):
            if a1 is None:
                return (a2, True)
            if a2 >= len(a2) or a1.val != a2[a2]:
                return (-1, False)
            a2 += 1
            v2 = False
            if a1.left is not None:
                v3 = a2
                if v3 < len(a2) and a1.left.val == a2[v3]:
                    a2, v4 = traverse(a1.left, a2)
                    if not v4:
                        return (-1, False)
                else:
                    if a1.right is None:
                        return (-1, False)
                    v1.append(a1.val)
                    v2 = True
                    a2, v4 = traverse(a1.right, a2)
                    if not v4:
                        return (-1, False)
                    a2, v4 = traverse(a1.left, a2)
                    if not v4:
                        return (-1, False)
            if not v2 and a1.right is not None:
                a2, v4 = traverse(a1.right, a2)
                if not v4:
                    return (-1, False)
            return (a2, True)
        v2, v3 = traverse(a1, 0)
        if v3 and v2 == len(a2):
            return v1
        return [-1]
