class C1(object):

    def moveSubTree(self, a1, a2, a3):
        """
        """

        def find_parents(a1, a2, a3, a4, a5, a6):
            if a1 in (a3, a4):
                a6[a1] = a2
                if len(a6) == 2:
                    return (True, a5)
            for v1 in a1.children:
                v2, v3 = find_parents(v1, a1, a3, a4, a5 or a1 == a3, a6)
                if v2:
                    return (True, v3)
            return (False, False)
        v1 = {}
        v2 = find_parents(a1, None, a2, a3, False, v1)[1]
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
