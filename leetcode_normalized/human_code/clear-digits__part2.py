class C1(object):

    def clearDigits(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v2.isdigit():
                v1.pop()
                continue
            v1.append(v2)
        return ''.join(v1)
