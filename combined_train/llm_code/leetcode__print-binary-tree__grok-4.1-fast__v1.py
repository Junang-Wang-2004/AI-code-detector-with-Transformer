class C1(object):

    def printTree(self, a1):
        if not a1:
            return []

        def depth(a1):
            if not a1:
                return 0
            return 1 + max(depth(a1.left), depth(a1.right))
        v1 = depth(a1)

        def span(a1):
            if not a1:
                return 0
            return 1 + 2 * max(span(a1.left), span(a1.right))
        v2 = span(a1)
        v3 = [['' for v4 in range(v2)] for v4 in range(v1)]
        v5 = []
        v5.append((a1, 0, v2 // 2))
        while v5:
            v6, v7, v8 = v5.pop(0)
            if v6:
                v3[v7][v8] = str(v6.val)
                v9 = 1 << v1 - v7 - 2
                if v6.left:
                    v5.append((v6.left, v7 + 1, v8 - v9))
                if v6.right:
                    v5.append((v6.right, v7 + 1, v8 + v9))
        return v3
