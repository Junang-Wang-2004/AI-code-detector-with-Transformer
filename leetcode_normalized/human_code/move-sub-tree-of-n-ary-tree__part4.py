class C1(object):

    def moveSubTree(self, a1, a2, a3):
        """
        """

        def find_parents(a1, a2, a3, a4, a5):
            if a1 in (a3, a4):
                a5[a1] = a2
                if len(a5) == 2:
                    return True
            for v1 in a1.children:
                if find_parents(v1, a1, a3, a4, a5):
                    return True
            return False

        def is_ancestor(a1, a2):
            for v1 in a1.children:
                if a1 == a2 or is_ancestor(v1, a2):
                    return True
            return False
        v1 = {}
        find_parents(a1, None, a2, a3, v1)
        if a2 in v1 and v1[a2] == a3:
            return a1
        a3.children.append(a2)
        if not is_ancestor(a2, a3):
            v1[a2].children.remove(a2)
        else:
            v1[a3].children.remove(a3)
            if a2 == a1:
                a1 = a3
            else:
                v1[a2].children[v1[a2].children.index(a2)] = a3
        return a1
