class C1(object):

    def encode(self, a1):
        """Encodes a list of strings to a single string.

        """
        v1 = ''
        for v2 in a1:
            v1 += '%0*x' % (8, len(v2)) + v2
        return v1

    def decode(self, a1):
        """Decodes a single string to a list of strings.

        """
        v1 = 0
        v2 = []
        while v1 < len(a1):
            v3 = int(a1[v1:v1 + 8], 16)
            v2.append(a1[v1 + 8:v1 + 8 + v3])
            v1 += 8 + v3
        return v2
