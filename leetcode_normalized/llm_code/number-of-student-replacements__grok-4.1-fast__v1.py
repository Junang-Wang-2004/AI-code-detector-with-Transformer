class C1(object):

    def totalReplacements(self, a1):
        v1 = []
        for v2 in a1:
            if not v1 or v2 < v1[-1]:
                v1.append(v2)
        return len(v1) - 1
