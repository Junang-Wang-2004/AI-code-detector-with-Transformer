class C1(object):

    def hIndex(self, a1):
        """
        """
        a1.sort(reverse=True)
        v1 = 0
        for v2 in a1:
            if v2 >= v1 + 1:
                v1 += 1
            else:
                break
        return v1
