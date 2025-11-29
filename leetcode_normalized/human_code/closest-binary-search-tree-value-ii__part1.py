class C1(object):

    def closestKValues(self, a1, a2, a3):
        """
        """

        def nextNode(a1, a2, a3):
            if a1:
                if a3(a1):
                    a1.append(a3(a1))
                    while a2(a1):
                        a1.append(a2(a1))
                else:
                    v1 = a1.pop()
                    while a1 and v1 is a3(a1):
                        v1 = a1.pop()
        v1 = lambda stack: stack[-1].left
        v2 = lambda stack: stack[-1].right
        v3 = []
        while a1:
            v3.append(a1)
            a1 = a1.left if a2 < a1.val else a1.right
        v5 = lambda node: abs(node.val - a2)
        v6 = v3[:v3.index(min(v3, key=v5)) + 1]
        v7 = list(v6)
        nextNode(v7, v1, v2)
        v8 = []
        for v9 in range(a3):
            if v6 and (not v7 or v5(v6[-1]) < v5(v7[-1])):
                v8.append(v6[-1].val)
                nextNode(v6, v2, v1)
            elif v7 and (not v6 or v5(v7[-1]) <= v5(v6[-1])):
                v8.append(v7[-1].val)
                nextNode(v7, v1, v2)
        return v8
