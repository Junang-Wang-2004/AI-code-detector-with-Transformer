class C1(object):

    def possiblyEquals(self, a1, a2):
        """
        """

        def memoization(a1, a2, a3, a4, a5, a6):
            if (a3, a4, a5) not in a6:
                if a3 == len(a1) and a4 == len(a2):
                    a6[a3, a4, a5] = a5 == 0
                elif a3 != len(a1) and a1[a3].isdigit():
                    a6[a3, a4, a5] = False
                    for v1 in range(a3 + 1, len(a1) + 1):
                        if (v1 == len(a1) or a1[v1] != '0') and memoization(a1, a2, v1, a4, a5 + int(a1[a3:v1]), a6):
                            a6[a3, a4, a5] = True
                            break
                        if v1 == len(a1) or not a1[v1].isdigit():
                            break
                elif a4 != len(a2) and a2[a4].isdigit():
                    a6[a3, a4, a5] = False
                    for v2 in range(a4 + 1, len(a2) + 1):
                        if (v2 == len(a2) or a2[v2] != '0') and memoization(a1, a2, a3, v2, a5 - int(a2[a4:v2]), a6):
                            a6[a3, a4, a5] = True
                            break
                        if v2 == len(a2) or not a2[v2].isdigit():
                            break
                elif a5 < 0:
                    a6[a3, a4, a5] = memoization(a1, a2, a3 + 1, a4, a5 + 1, a6) if a3 != len(a1) else False
                elif a5 > 0:
                    a6[a3, a4, a5] = memoization(a1, a2, a3, a4 + 1, a5 - 1, a6) if a4 != len(a2) else False
                else:
                    a6[a3, a4, a5] = memoization(a1, a2, a3 + 1, a4 + 1, a5, a6) if a3 != len(a1) and a4 != len(a2) and (a1[a3] == a2[a4]) else False
            return a6[a3, a4, a5]
        return memoization(a1, a2, 0, 0, 0, {})
