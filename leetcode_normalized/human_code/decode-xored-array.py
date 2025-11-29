class C1(object):

    def decode(self, a1, a2):
        """
        """
        v1 = [a2]
        for v2 in a1:
            v1.append(v1[-1] ^ v2)
        return v1
