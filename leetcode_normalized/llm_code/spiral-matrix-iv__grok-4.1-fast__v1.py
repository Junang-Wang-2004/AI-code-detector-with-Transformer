class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def spiralMatrix(self, a1, a2, a3):
        v1 = [[-1 for v2 in range(a2)] for v2 in range(a1)]
        v3, v4 = (0, a2 - 1)
        v5, v6 = (0, a1 - 1)
        v7 = a3
        while v7 and v5 <= v6 and (v3 <= v4):
            for v8 in range(v3, v4 + 1):
                if not v7:
                    break
                v1[v5][v8] = v7.val
                v7 = v7.next
            v5 += 1
            for v9 in range(v5, v6 + 1):
                if not v7:
                    break
                v1[v9][v4] = v7.val
                v7 = v7.next
            v4 -= 1
            if v5 <= v6:
                for v8 in range(v4, v3 - 1, -1):
                    if not v7:
                        break
                    v1[v6][v8] = v7.val
                    v7 = v7.next
                v6 -= 1
            if v3 <= v4:
                for v9 in range(v6, v5 - 1, -1):
                    if not v7:
                        break
                    v1[v9][v3] = v7.val
                    v7 = v7.next
                v3 += 1
        return v1
