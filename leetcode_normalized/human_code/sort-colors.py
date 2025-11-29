class C1(object):

    def sortColors(self, a1):
        """
        """

        def triPartition(a1, a2):
            v1, v2, v3 = (0, 0, len(a1) - 1)
            while v1 <= v3:
                if a1[v1] > a2:
                    a1[v1], a1[v3] = (a1[v3], a1[v1])
                    v3 -= 1
                else:
                    if a1[v1] < a2:
                        a1[v2], a1[v1] = (a1[v1], a1[v2])
                        v2 += 1
                    v1 += 1
        triPartition(a1, 1)
