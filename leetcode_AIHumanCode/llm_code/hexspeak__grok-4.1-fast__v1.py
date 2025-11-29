class Solution:
    def toHexspeak(self, num):
        hex_digits = format(int(num), 'X')
        mapping = {'0': 'O', '1': 'I'}
        parts = []
        for d in hex_digits:
            if d in mapping:
                parts.append(mapping[d])
            elif d.isalpha():
                parts.append(d)
            else:
                return "ERROR"
        return "".join(parts)
