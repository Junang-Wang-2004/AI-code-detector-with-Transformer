class C1(object):

    def decodeCiphertext(self, a1, a2):
        """
        """
        v1 = len(a1) // a2
        v2 = []
        for v3 in range(v1):
            for v4 in range(v3, len(a1), v1 + 1):
                v2.append(a1[v4])
        while v2 and v2[-1] == ' ':
            v2.pop()
        return ''.join(v2)
