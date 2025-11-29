class C1(object):

    def readBinaryWatch(self, a1):
        """
        """

        def bit_count(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        return ['%d:%02d' % (h, m) for v1 in range(12) for v2 in range(60) if bit_count(v1) + bit_count(v2) == a1]

    def readBinaryWatch2(self, a1):
        """
        """
        return ['{0}:{1}'.format(str(h), str(m).zfill(2)) for v1 in range(12) for v2 in range(60) if (bin(v1) + bin(v2)).count('1') == a1]
