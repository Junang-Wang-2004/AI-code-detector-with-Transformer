class C1(object):

    def verifyPreorder(self, a1):
        v1, v2 = (float('-inf'), -1)
        for v3 in a1:
            if v3 < v1:
                return False
            while v2 >= 0 and v3 > a1[v2]:
                v1 = a1[v2]
                v2 -= 1
            v2 += 1
            a1[v2] = v3
        return True
