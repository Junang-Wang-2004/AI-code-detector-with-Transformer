class C1(object):

    def removeDuplicates(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v1 and v1[-1] == v2:
                v1.pop()
            else:
                v1.append(v2)
        return ''.join(v1)
