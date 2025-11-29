class C1(object):

    def countValidWords(self, a1):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in range(len(a1) + 1):
            if v4 == len(a1) or a1[v4] == ' ':
                if v2 == 1:
                    v1 += 1
                v2 = v3 = 0
                continue
            if a1[v4].isdigit() or (a1[v4] in '!.,' and (not (v4 == len(a1) - 1 or a1[v4 + 1] == ' '))) or (a1[v4] == '-' and (not (v3 == 0 and 0 < v4 < len(a1) - 1 and a1[v4 - 1].isalpha() and a1[v4 + 1].isalpha()))):
                v2 = -1
                continue
            if v2 == 0:
                v2 = 1
            if a1[v4] == '-':
                v3 = 1
        return v1
