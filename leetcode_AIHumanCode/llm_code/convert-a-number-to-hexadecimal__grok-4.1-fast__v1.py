class Solution(object):
    def toHex(self, num):
        hexmap = '0123456789abcdef'
        chunks = []
        while len(chunks) < 8:
            remainder = num % 16
            chunks.append(hexmap[remainder])
            num //= 16
            if num == 0:
                break
        chunks.reverse()
        return ''.join(chunks)
