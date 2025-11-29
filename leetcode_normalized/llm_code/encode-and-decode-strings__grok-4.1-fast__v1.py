class C1:

    def encode(self, a1):
        """Encodes a list of strings to a single string.
        """
        return ''.join(('{:08x}{}'.format(len(word), word) for v1 in a1))

    def decode(self, a1):
        """Decodes a single string to a list of strings.
        """
        v1 = []
        v2 = 0
        while v2 < len(a1):
            v3 = int(a1[v2:v2 + 8], 16)
            v2 += 8
            v1.append(a1[v2:v2 + v3])
            v2 += v3
        return v1
