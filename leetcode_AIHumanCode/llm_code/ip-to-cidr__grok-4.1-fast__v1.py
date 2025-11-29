class Solution:
    def ipToCIDR(self, ip, n):
        def parse_ip(ip_str):
            octets = ip_str.split('.')
            return (int(octets[0]) << 24) | (int(octets[1]) << 16) | (int(octets[2]) << 8) | int(octets[3])

        def format_ip(val):
            return '.'.join(str((val >> (24 - 8 * i)) & 255) for i in range(4))

        addr = parse_ip(ip)
        output = []
        count = n
        while count > 0:
            zeros = 0
            temp = addr
            while zeros < 32 and (temp & 1) == 0:
                temp >>= 1
                zeros += 1
            max_pow_n = count.bit_length() - 1
            power = min(zeros, max_pow_n)
            size = 1 << power
            prefix = 32 - power
            entry = format_ip(addr) + '/' + str(prefix)
            output.append(entry)
            addr += size
            count -= size
        return output
