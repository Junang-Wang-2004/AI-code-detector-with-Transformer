class C1(object):

    def similarRGB(self, a1):
        """
        """

        def rounding(a1):
            v1, v2 = divmod(int(a1, 16), 17)
            if v2 > 8:
                v1 += 1
            return '{:02x}'.format(17 * v1)
        return '#' + rounding(a1[1:3]) + rounding(a1[3:5]) + rounding(a1[5:7])
