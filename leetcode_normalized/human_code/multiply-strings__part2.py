class C1(object):

    def multiply(self, a1, a2):
        """
        """
        a1, a2 = (a1[::-1], a2[::-1])
        v3 = [0] * (len(a1) + len(a2))
        for v4 in range(len(a1)):
            for v5 in range(len(a2)):
                v3[v4 + v5] += int(a1[v4]) * int(a2[v5])
                v3[v4 + v5 + 1] += v3[v4 + v5] // 10
                v3[v4 + v5] %= 10
        for v4 in reversed(range(len(v3))):
            if v3[v4]:
                break
        return ''.join(map(str, v3[v4::-1]))
