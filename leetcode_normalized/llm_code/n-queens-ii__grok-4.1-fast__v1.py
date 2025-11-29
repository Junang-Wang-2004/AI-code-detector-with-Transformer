class C1:

    def totalNQueens(self, a1):

        def search(a1, a2):
            if a1 == a1:
                return 1
            v1 = 0
            for v2 in range(a1):
                if safe(a2, a1, v2):
                    a2[a1] = v2
                    v1 += search(a1 + 1, a2)
            return v1

        def safe(a1, a2, a3):
            for v1 in range(a2):
                v2 = a1[v1]
                if v2 == a3 or abs(v1 - a2) == abs(v2 - a3):
                    return False
            return True
        v1 = [-1] * a1
        return search(0, v1)
