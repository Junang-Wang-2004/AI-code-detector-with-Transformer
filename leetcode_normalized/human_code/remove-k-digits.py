class C1(object):

    def removeKdigits(self, a1, a2):
        """
        """
        v1 = []
        for v2 in a1:
            while a2 and v1 and (v1[-1] > v2):
                v1.pop()
                a2 -= 1
            v1.append(v2)
        return ''.join(v1).lstrip('0')[:-a2 or None] or '0'
