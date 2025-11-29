class C1:

    def moveSubTree(self, a1, a2, a3):

        def get_parent(a1, a2):
            if a1 == a2:
                return None
            v1 = [(a1, None)]
            while v1:
                v2, v3 = v1.pop()
                if v2 == a2:
                    return v3
                for v4 in v2.children:
                    v1.append((v4, v2))
            return None

        def has_sub(a1, a2):
            v1 = [a1]
            while v1:
                v2 = v1.pop()
                if v2 == a2:
                    return True
                for v3 in v2.children:
                    v1.append(v3)
            return False
        v1 = get_parent(a1, a2)
        v2 = get_parent(a1, a3)
        if v1 == a3:
            return a1
        v3 = has_sub(a2, a3)
        a3.children.append(a2)
        if not v3:
            if v1 is not None:
                v1.children.remove(a2)
        else:
            v2.children.remove(a3)
            if v1 is None:
                a1 = a3
            else:
                v5 = v1.children.index(a2)
                v1.children[v5] = a3
        return a1
