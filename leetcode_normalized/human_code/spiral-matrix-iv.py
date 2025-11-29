class C1(object):

    def __init__(self, a1=0, a2=None):
        pass

class C2(object):

    def spiralMatrix(self, a1, a2, a3):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = [[-1] * a2 for v3 in range(a1)]
        v4 = v5 = v6 = 0
        while a3:
            v2[v4][v5] = a3.val
            if not (0 <= v4 + v1[v6][0] < a1 and 0 <= v5 + v1[v6][1] < a2 and (v2[v4 + v1[v6][0]][v5 + v1[v6][1]] == -1)):
                v6 = (v6 + 1) % 4
            v4, v5 = (v4 + v1[v6][0], v5 + v1[v6][1])
            a3 = a3.__next__
        return v2
