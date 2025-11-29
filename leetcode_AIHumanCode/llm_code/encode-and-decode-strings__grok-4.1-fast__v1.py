class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        return ''.join("{:08x}{}".format(len(word), word) for word in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        output = []
        pos = 0
        while pos < len(s):
            size = int(s[pos:pos + 8], 16)
            pos += 8
            output.append(s[pos:pos + size])
            pos += size
        return output
