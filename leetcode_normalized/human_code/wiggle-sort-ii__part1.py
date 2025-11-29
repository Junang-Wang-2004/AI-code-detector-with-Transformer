class C1(object):

    def wiggleSort(self, a1):
        """
        """
        a1.sort()
        v1 = (len(a1) - 1) / 2
        a1[::2], a1[1::2] = (a1[v1::-1], a1[:v1:-1])
