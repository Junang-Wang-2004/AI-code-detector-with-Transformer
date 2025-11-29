class C1(object):

    def wiggleSort(self, a1):
        """
        """
        for v1 in range(1, len(a1)):
            if v1 % 2 and a1[v1 - 1] > a1[v1] or (not v1 % 2 and a1[v1 - 1] < a1[v1]):
                a1[v1 - 1], a1[v1] = (a1[v1], a1[v1 - 1])
