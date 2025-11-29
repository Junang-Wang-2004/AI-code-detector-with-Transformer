class C1(object):

    def verifyPreorder(self, a1):
        v1 = float('-inf')
        v2 = []
        for v3 in a1:
            if v3 < v1:
                return False
            while v2 and v3 > v2[-1]:
                v1 = v2[-1]
                v2.pop()
            v2.append(v3)
        return True
