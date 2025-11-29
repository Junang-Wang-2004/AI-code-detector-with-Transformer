class C1(object):

    def decodeMessage(self, a1, a2):
        v1 = {}
        v2 = ord('a')
        for v3 in a1:
            if 'a' <= v3 <= 'z' and v3 not in v1:
                v1[v3] = chr(v2)
                v2 += 1
        return ''.join((v1.get(v3, v3) for v3 in a2))
