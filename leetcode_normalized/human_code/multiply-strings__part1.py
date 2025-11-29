class C1(object):

    def multiply(self, a1, a2):
        """
        """
        v1 = [0] * (len(a1) + len(a2))
        for v2 in reversed(range(len(a1))):
            for v3 in reversed(range(len(a2))):
                v1[v2 + v3 + 1] += int(a1[v2]) * int(a2[v3])
                v1[v2 + v3] += v1[v2 + v3 + 1] // 10
                v1[v2 + v3 + 1] %= 10
        for v2 in range(len(v1)):
            if v1[v2]:
                break
        return ''.join([str(x) for v4 in v1[v2:]])
