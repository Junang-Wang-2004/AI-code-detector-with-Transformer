class C1(object):

    def isPreorder(self, a1):
        if not a1:
            return False
        v1 = [a1[0][0]]
        for v2 in range(1, len(a1)):
            v3 = a1[v2][1]
            while v1 and v1[-1] != v3:
                v1.pop()
            if not v1:
                return False
            v1.append(a1[v2][0])
        return True
