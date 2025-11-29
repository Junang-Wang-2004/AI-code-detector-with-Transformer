class C1(object):

    def possiblyEquals(self, a1, a2):
        """
        """

        def general_possible_numbers(a1):
            v1 = [set() for v2 in range(len(a1))]
            for v3 in range(len(a1)):
                v4, v5 = (0, 1)
                for v6 in reversed(range(v3 + 1)):
                    v4 += int(a1[v6]) * v5
                    v5 *= 10
                    if a1[v6] == '0':
                        continue
                    if v6 == 0:
                        v1[v3].add(v4)
                    else:
                        v1[v3].update((x + v4 for v7 in v1[v6 - 1]))
            return v1[-1]

        def optimized_possible_numbers(a1):
            assert len(a1) <= 3
            v1 = {int(a1)}
            if len(a1) >= 2:
                if a1[1] != '0':
                    v1.add(int(a1[:1]) + int(a1[1:]))
            if len(a1) >= 3:
                if a1[2] != '0':
                    v1.add(int(a1[:2]) + int(a1[2:]))
                    if a1[1] != '0':
                        v1.add(int(a1[0:1]) + int(a1[1:2]) + int(a1[2:]))
            return v1

        def memoization(a1, a2, a3, a4, a5, a6):
            if (a3, a4, a5) not in a6:
                if a3 == len(a1) and a4 == len(a2):
                    a6[a3, a4, a5] = a5 == 0
                elif a3 != len(a1) and a1[a3].isdigit():
                    a6[a3, a4, a5] = False
                    for v1 in range(a3 + 1, len(a1) + 1):
                        if v1 == len(a1) or not a1[v1].isdigit():
                            break
                    for v2 in optimized_possible_numbers(a1[a3:v1]):
                        if memoization(a1, a2, v1, a4, a5 + v2, a6):
                            a6[a3, a4, a5] = True
                            break
                elif a4 != len(a2) and a2[a4].isdigit():
                    a6[a3, a4, a5] = False
                    for v3 in range(a4 + 1, len(a2) + 1):
                        if v3 == len(a2) or not a2[v3].isdigit():
                            break
                    for v2 in optimized_possible_numbers(a2[a4:v3]):
                        if memoization(a1, a2, a3, v3, a5 - v2, a6):
                            a6[a3, a4, a5] = True
                            break
                elif a5 < 0:
                    a6[a3, a4, a5] = memoization(a1, a2, a3 + 1, a4, a5 + 1, a6) if a3 != len(a1) else False
                elif a5 > 0:
                    a6[a3, a4, a5] = memoization(a1, a2, a3, a4 + 1, a5 - 1, a6) if a4 != len(a2) else False
                else:
                    a6[a3, a4, a5] = memoization(a1, a2, a3 + 1, a4 + 1, a5, a6) if a3 != len(a1) and a4 != len(a2) and (a1[a3] == a2[a4]) else False
            return a6[a3, a4, a5]
        return memoization(a1, a2, 0, 0, 0, {})
