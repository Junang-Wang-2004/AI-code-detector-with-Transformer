class C1(object):

    def __init__(self, a1=None, a2=None):
        self.val = a1
        self.children = a2 if a2 is not None else []

class C2(object):

    def moveSubTree(self, a1, a2, a3):
        """
        """

        def iter_find_parents(a1, a2, a3, a4, a5, a6):
            v1 = [(1, [a1, None, False])]
            while v1:
                v2, v3 = v1.pop()
                if v2 == 1:
                    a1, a2, a5 = v3
                    if a1 in (a3, a4):
                        a6[a1] = a2
                        if len(a6) == 2:
                            return a5
                    v1.append((2, [a1, a5, reversed(a1.children)]))
                else:
                    a1, a5, v7 = v3
                    v8 = next(v7, None)
                    if not v8:
                        continue
                    v1.append((2, [a1, a5, v7]))
                    v1.append((1, [v8, a1, a5 or a1 == a3]))
            assert False
            return False
        v1 = {}
        v2 = iter_find_parents(a1, None, a2, a3, False, v1)
        if a2 in v1 and v1[a2] == a3:
            return a1
        a3.children.append(a2)
        if not v2:
            v1[a2].children.remove(a2)
        else:
            v1[a3].children.remove(a3)
            if a2 == a1:
                a1 = a3
            else:
                v1[a2].children[v1[a2].children.index(a2)] = a3
        return a1
