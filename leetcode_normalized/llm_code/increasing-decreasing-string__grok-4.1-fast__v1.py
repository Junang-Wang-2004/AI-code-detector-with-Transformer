import string

class C1:

    def sortString(self, a1):
        v1 = string.ascii_lowercase
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - 97] += 1
        v4 = []
        v5 = True
        v6 = len(a1)
        while len(v4) < v6:
            if v5:
                for v7 in range(26):
                    if v2[v7] > 0:
                        v4.append(v1[v7])
                        v2[v7] -= 1
            else:
                for v7 in range(25, -1, -1):
                    if v2[v7] > 0:
                        v4.append(v1[v7])
                        v2[v7] -= 1
            v5 = not v5
        return ''.join(v4)
