class C1(object):

    def reverseWords(self, a1):
        v1, v2 = (0, len(a1) - 1)
        while v1 < v2:
            a1[v1], a1[v2] = (a1[v2], a1[v1])
            v1 += 1
            v2 -= 1
        v3 = 0
        while v3 < len(a1):
            while v3 < len(a1) and a1[v3] == ' ':
                v3 += 1
            if v3 >= len(a1):
                break
            v4 = v3
            while v4 < len(a1) and a1[v4] != ' ':
                v4 += 1
            v5, v6 = (v3, v4 - 1)
            while v5 < v6:
                a1[v5], a1[v6] = (a1[v6], a1[v5])
                v5 += 1
                v6 -= 1
            v3 = v4
