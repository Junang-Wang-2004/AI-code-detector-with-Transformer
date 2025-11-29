class C1(object):

    def moveSubTree(self, a1, a2, a3):
        """
        """

        def iter_find_parents(a1, a2, a3, a4, a5):
            v1 = [(1, [a1, None])]
            while v1:
                v2, v3 = v1.pop()
                if v2 == 1:
                    a1, a2 = v3
                    if a1 in (a3, a4):
                        a5[a1] = a2
                        if len(a5) == 2:
                            return
                    v1.append((2, [a1, reversed(a1.children)]))
                else:
                    a1, v6 = v3
                    v7 = next(v6, None)
                    if not v7:
                        continue
                    v1.append((2, [a1, v6]))
                    v1.append((1, [v7, a1]))

        def iter_is_ancestor(a1, a2):
            v1 = [(1, [a1])]
            while v1:
                v2, v3 = v1.pop()
                if v2 == 1:
                    a1 = v3[0]
                    v1.append((2, [reversed(a1.children)]))
                else:
                    v5 = v3[0]
                    v6 = next(v5, None)
                    if not v6:
                        continue
                    if v6 == a2:
                        return True
                    v1.append((2, [v5]))
                    v1.append((1, [v6]))
            return False
        v1 = {}
        iter_find_parents(a1, None, a2, a3, v1)
        if a2 in v1 and v1[a2] == a3:
            return a1
        a3.children.append(a2)
        if not iter_is_ancestor(a2, a3):
            v1[a2].children.remove(a2)
        else:
            v1[a3].children.remove(a3)
            if a2 == a1:
                a1 = a3
            else:
                v1[a2].children[v1[a2].children.index(a2)] = a3
        return a1
