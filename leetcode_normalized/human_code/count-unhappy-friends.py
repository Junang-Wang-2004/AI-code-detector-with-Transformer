class C1(object):

    def unhappyFriends(self, a1, a2, a3):
        """
        """
        v1 = [[0] * a1 for v2 in range(a1)]
        for v3 in range(len(a2)):
            for v4 in range(len(a2[v3])):
                v1[v3][a2[v3][v4]] = v4
        v5 = [0] * a1
        for v3, v4 in a3:
            v5[v3], v5[v4] = (v4, v3)
        return sum((any((v1[v3][v4] < v1[v3][v5[v3]] and v1[v4][v3] < v1[v4][v5[v4]] for v4 in range(len(v1[v3])) if v4 != v3 and v4 != v5[v3])) for v3 in range(len(v1))))
