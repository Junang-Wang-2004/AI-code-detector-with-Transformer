import itertools

class C1(object):

    def decodeMessage(self, a1, a2):
        """
        """
        v1 = lambda x: ord(x) - ord('a')
        v2 = [-1] * 26
        v3 = 0
        for v4 in map(v1, a1):
            if v4 < 0 or v2[v4] != -1:
                continue
            v2[v4] = v3
            v3 += 1
        return ''.join(map(lambda x: chr(ord('a') + v4), (v2[v4] if v4 >= 0 else v4 for v4 in map(v1, a2))))
