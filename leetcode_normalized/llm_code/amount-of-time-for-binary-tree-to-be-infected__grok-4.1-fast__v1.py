class C1(object):

    def amountOfTime(self, a1, a2):

        def locate_start(a1):
            if not a1:
                return None
            v1 = [a1]
            while v1:
                v2 = v1.pop()
                if v2.val == a2:
                    return v2
                if v2.right:
                    v1.append(v2.right)
                if v2.left:
                    v1.append(v2.left)
            return None
        v1 = locate_start(a1)
        v2 = set([v1])
        v3 = [v1]
        v4 = 0
        while v3:
            v5 = []
            for v6 in v3:
                for v7 in (v6.left, v6.right):
                    if v7 and v7 not in v2:
                        v2.add(v7)
                        v5.append(v7)
            v3 = v5
            if v3:
                v4 += 1
        return v4
