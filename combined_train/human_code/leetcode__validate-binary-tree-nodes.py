class C1(object):

    def validateBinaryTreeNodes(self, a1, a2, a3):
        """
        """
        v1 = set(range(a1)) - set(a2) - set(a3)
        if len(v1) != 1:
            return False
        v2, = v1
        v3 = [v2]
        v4 = set([v2])
        while v3:
            v5 = v3.pop()
            for v6 in (a2[v5], a3[v5]):
                if v6 < 0:
                    continue
                if v6 in v4:
                    return False
                v4.add(v6)
                v3.append(v6)
        return len(v4) == a1
