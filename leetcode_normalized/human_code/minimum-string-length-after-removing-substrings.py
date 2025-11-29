class C1(object):

    def minLength(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v1 and (v1[-1] == 'A' and v2 == 'B' or (v1[-1] == 'C' and v2 == 'D')):
                v1.pop()
                continue
            v1.append(v2)
        return len(v1)
