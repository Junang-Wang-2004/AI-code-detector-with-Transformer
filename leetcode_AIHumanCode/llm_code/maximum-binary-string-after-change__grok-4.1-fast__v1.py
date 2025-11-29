class Solution:
    def maximumBinaryString(self, binary):
        z = binary.count('0')
        if z == 0:
            return binary
        f = binary.find('0')
        p = f + z - 1
        n = len(binary)
        return '1' * p + '0' + '1' * (n - p - 1)
