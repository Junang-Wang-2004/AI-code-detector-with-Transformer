class C1:

    def ipToCIDR(self, a1, a2):

        def parse_ip(a1):
            v1 = a1.split('.')
            return int(v1[0]) << 24 | int(v1[1]) << 16 | int(v1[2]) << 8 | int(v1[3])

        def format_ip(a1):
            return '.'.join((str(a1 >> 24 - 8 * i & 255) for v1 in range(4)))
        v1 = parse_ip(a1)
        v2 = []
        v3 = a2
        while v3 > 0:
            v4 = 0
            v5 = v1
            while v4 < 32 and v5 & 1 == 0:
                v5 >>= 1
                v4 += 1
            v6 = v3.bit_length() - 1
            v7 = min(v4, v6)
            v8 = 1 << v7
            v9 = 32 - v7
            v10 = format_ip(v1) + '/' + str(v9)
            v2.append(v10)
            v1 += v8
            v3 -= v8
        return v2
