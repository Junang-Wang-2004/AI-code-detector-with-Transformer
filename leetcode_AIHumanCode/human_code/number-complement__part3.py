# Time:  O(1)
# Space: O(1)

class Solution3(object):
    def findComplement(self, num):
        bits = '{0:b}'.format(num)
        complement_bits = ''.join('1' if bit == '0' else '0' for bit in bits)
        return int(complement_bits, 2)

