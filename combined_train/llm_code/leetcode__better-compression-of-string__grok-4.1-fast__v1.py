class C1(object):

    def betterCompression(self, a1):
        v1 = [0] * 26
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = a1[v2]
            v5 = ord(v4) - ord('a')
            v2 += 1
            v6 = ''
            while v2 < v3 and a1[v2].isdigit():
                v6 += a1[v2]
                v2 += 1
            if v6:
                v1[v5] += int(v6)
        v7 = []
        for v8 in range(26):
            if v1[v8] > 0:
                v7.append(chr(ord('a') + v8) + str(v1[v8]))
        return ''.join(v7)
