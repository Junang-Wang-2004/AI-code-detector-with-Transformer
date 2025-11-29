class C1(object):

    def validateStackSequences(self, a1, a2):
        """
        """
        v1 = 0
        v2 = []
        for v3 in a1:
            v2.append(v3)
            while v2 and v1 < len(a2) and (v2[-1] == a2[v1]):
                v2.pop()
                v1 += 1
        return v1 == len(a2)
