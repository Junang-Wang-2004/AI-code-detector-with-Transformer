class C1(object):

    def hasMatch(self, a1, a2):
        v1 = [part for v2 in a2.split('*') if v2]
        v3 = 0
        for v2 in v1:
            v4 = a1.find(v2, v3)
            if v4 == -1:
                return False
            v3 = v4 + len(v2)
        return True
