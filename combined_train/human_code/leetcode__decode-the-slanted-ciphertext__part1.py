class C1(object):

    def decodeCiphertext(self, a1, a2):
        """
        """
        v1 = len(a1) // a2
        v2 = len(a1)
        for v3 in reversed(range(v1)):
            for v4 in reversed(range(v3, len(a1), v1 + 1)):
                if a1[v4] != ' ':
                    v2 = v4
                    break
            else:
                continue
            break
        v5 = []
        for v3 in range(v1):
            for v4 in range(v3, len(a1), v1 + 1):
                v5.append(a1[v4])
                if v4 == v2:
                    break
            else:
                continue
            break
        return ''.join(v5)
