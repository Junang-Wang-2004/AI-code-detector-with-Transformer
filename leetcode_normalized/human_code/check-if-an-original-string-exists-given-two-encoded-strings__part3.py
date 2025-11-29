class C1(object):

    def possiblyEquals(self, a1, a2):
        """
        """
        v1 = 3
        v2 = 1 + v1
        v3 = [[set() for v4 in range(len(a2) + 1)] for v4 in range(v2)]
        v3[0][0].add(0)
        for v5 in range(len(a1) + 1):
            if v5:
                v3[(v5 - 1) % v2] = [set() for v4 in range(len(a2) + 1)]
            if v5 != len(a1) and a1[v5] == '0':
                continue
            for v6 in range(len(a2) + 1):
                for v7 in v3[v5 % v2][v6]:
                    if v5 != len(a1) and v6 != len(a2) and (a1[v5] == a2[v6]) and (v7 == 0):
                        v3[(v5 + 1) % v2][v6 + 1].add(v7)
                    if v7 <= 0 and v5 != len(a1):
                        if not a1[v5].isdigit():
                            if v7:
                                v3[(v5 + 1) % v2][v6].add(v7 + 1)
                        elif a1[v5] != '0':
                            v8 = 0
                            for v9 in range(v5, len(a1)):
                                if not a1[v9].isdigit():
                                    break
                                v8 = v8 * 10 + int(a1[v9])
                                v3[(v9 + 1) % v2][v6].add(v7 + v8)
                    if v7 >= 0 and v6 != len(a2):
                        if not a2[v6].isdigit():
                            if v7:
                                v3[v5 % v2][v6 + 1].add(v7 - 1)
                        elif a2[v6] != '0':
                            v8 = 0
                            for v10 in range(v6, len(a2)):
                                if not a2[v10].isdigit():
                                    break
                                v8 = v8 * 10 + int(a2[v10])
                                v3[v5 % v2][v10 + 1].add(v7 - v8)
        return 0 in v3[len(a1) % v2][len(a2)]
