class C1:

    def isSubsequence(self, a1, a2):
        v1 = 0
        for v2 in a1:
            v1 = a2.find(v2, v1)
            if v1 == -1:
                return False
            v1 += 1
        return True
