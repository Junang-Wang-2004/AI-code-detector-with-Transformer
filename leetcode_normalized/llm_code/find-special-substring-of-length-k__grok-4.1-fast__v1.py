class C1(object):

    def hasSpecialSubstring(self, a1, a2):
        v1 = 0
        v2 = len(a1)
        while v1 < v2:
            v3 = v1 + 1
            while v3 < v2 and a1[v3] == a1[v1]:
                v3 += 1
            if v3 - v1 == a2:
                return True
            v1 = v3
        return False
