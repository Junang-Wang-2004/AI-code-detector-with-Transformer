class C1(object):

    def numberOfChild(self, a1, a2):
        v1 = a1 - 1
        v2 = 2 * v1
        v3 = a2 % v2
        return v3 if v3 <= v1 else v2 - v3
