class C1(object):

    def shortestPalindrome(self, a1):
        v1 = a1[::-1]
        v2 = a1 + '#' + v1
        v3 = len(v2)
        v4 = [0] * v3
        v5 = 0
        v6 = 1
        while v6 < v3:
            if v2[v6] == v2[v5]:
                v5 += 1
                v4[v6] = v5
                v6 += 1
            elif v5 != 0:
                v5 = v4[v5 - 1]
            else:
                v4[v6] = 0
                v6 += 1
        v7 = v4[-1]
        return a1[v7:][::-1] + a1
