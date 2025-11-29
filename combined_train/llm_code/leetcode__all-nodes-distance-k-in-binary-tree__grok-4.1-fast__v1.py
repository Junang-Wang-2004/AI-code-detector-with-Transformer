class C1(object):

    def distanceK(self, a1, a2, a3):
        if a3 == 0:
            return [a2.val]

        def gather(a1, a2, a3):
            if a1 is None or a2 < 0:
                return
            if a2 == 0:
                a3.append(a1.val)
                return
            gather(a1.left, a2 - 1, a3)
            gather(a1.right, a2 - 1, a3)
        v1 = []
        gather(a2.left, a3 - 1, v1)
        gather(a2.right, a3 - 1, v1)
        v2 = []

        def trace(a1, a2):
            if a1 is None:
                return False
            v2.append(a1)
            if a1 == a2:
                return True
            if trace(a1.left, a2) or trace(a1.right, a2):
                return True
            v2.pop()
            return False
        trace(a1, a2, v2)
        for v3 in range(len(v2) - 2, -1, -1):
            v4 = len(v2) - 1 - v3
            if v4 > a3:
                continue
            v5 = a3 - v4
            v6 = v2[v3]
            if v5 == 0:
                v1.append(v6.val)
                continue
            v7 = v2[v3 + 1]
            for v8 in (v6.left, v6.right):
                if v8 is not None and v8 != v7:
                    gather(v8, v5 - 1, v1)
        return v1
