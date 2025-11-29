class C1(object):

    def ipToCIDR(self, a1, a2):
        """
        """

        def ipToInt(a1):
            v1 = 0
            for v2 in a1.split('.'):
                v1 = 256 * v1 + int(v2)
            return v1

        def intToIP(a1):
            return '.'.join((str((a1 >> i) % 256) for v1 in (24, 16, 8, 0)))
        v1 = ipToInt(a1)
        v2 = []
        while a2:
            v3 = max(33 - (v1 & ~(v1 - 1)).bit_length(), 33 - a2.bit_length())
            v2.append(intToIP(v1) + '/' + str(v3))
            v1 += 1 << 32 - v3
            a2 -= 1 << 32 - v3
        return v2
