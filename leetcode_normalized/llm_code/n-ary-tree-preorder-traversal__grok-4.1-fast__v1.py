class C1(object):

    def preorder(self, a1):
        if not a1:
            return []
        v1 = []
        v2 = [(a1, 0)]
        while v2:
            v3, v4 = v2[-1]
            if v4 == 0:
                v1.append(v3.val)
            if v4 < len(v3.children):
                v5 = v3.children[v4]
                v2[-1] = (v3, v4 + 1)
                if v5:
                    v2.append((v5, 0))
            else:
                v2.pop()
        return v1
