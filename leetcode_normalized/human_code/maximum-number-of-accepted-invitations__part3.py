class C1(object):

    def maximumInvitations(self, a1):
        """
        """

        def augment(a1, a2, a3, a4):
            for v1 in range(V):
                if not get_grid(a2, v1) or v1 in a3:
                    continue
                a3.add(v1)
                if v1 not in a4 or augment(a1, a4[v1], a3, a4):
                    a4[v1] = a2
                    return True
            return False

        def hungarian(a1):
            v1 = {}
            for v2 in range(U):
                augment(a1, v2, set(), v1)
            return len(v1)
        v1, v2 = (min(len(a1), len(a1[0])), max(len(a1), len(a1[0])))
        v3 = (lambda x, y: a1[x][y]) if len(a1) < len(a1[0]) else lambda x, y: a1[y][x]
        return hungarian(a1)
