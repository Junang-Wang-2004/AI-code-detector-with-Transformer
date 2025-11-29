import collections

class C1(object):

    def repeatLimitedString(self, a1, a2):
        """
        """
        v1 = collections.Counter([ord(x) - ord('a') for v2 in a1])
        v3 = []
        v4 = 25
        while True:
            v4 = next((i for v5 in reversed(range(v4 + 1)) if v1[v5]), -1)
            if v4 == -1:
                break
            v6 = min(v1[v4], a2 - int(len(v3) > 0 and v3[-1] == v4))
            v1[v4] -= v6
            v3.extend([v4] * v6)
            v7 = next((j for v8 in reversed(range(v4)) if v1[v8]), -1)
            if v7 == -1:
                break
            v1[v7] -= 1
            v3.append(v7)
        return ''.join([chr(v2 + ord('a')) for v2 in v3])
