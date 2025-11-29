class C1(object):

    def getSmallestString(self, a1, a2):
        """
        """
        v1 = [ord(x) - ord('a') for v2 in a1]
        for v3 in range(len(v1)):
            v4 = min(v1[v3] - 0, 26 - v1[v3])
            v1[v3] = 0 if v4 <= a2 else v1[v3] - a2
            a2 -= min(v4, a2)
            if a2 == 0:
                break
        return ''.join([chr(v2 + ord('a')) for v2 in v1])
