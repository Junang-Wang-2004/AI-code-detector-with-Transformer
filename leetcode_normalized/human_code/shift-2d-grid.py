class C1(object):

    def shiftGrid(self, a1, a2):
        """
        """

        def rotate(a1, a2):

            def reverse(a1, a2, a3):
                while a2 < a3:
                    v1, v2 = divmod(a2, len(a1[0]))
                    v3, v4 = divmod(a3 - 1, len(a1[0]))
                    a1[v1][v2], a1[v3][v4] = (a1[v3][v4], a1[v1][v2])
                    a2 += 1
                    a3 -= 1
            a2 %= len(a1) * len(a1[0])
            reverse(a1, 0, len(a1) * len(a1[0]))
            reverse(a1, 0, a2)
            reverse(a1, a2, len(a1) * len(a1[0]))
        rotate(a1, a2)
        return a1
