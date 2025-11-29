from fractions import Fraction

class C1:

    def judgePoint24(self, a1):

        def possible(a1):
            if len(a1) == 1:
                return a1[0] == Fraction(24)
            for v1 in range(len(a1)):
                for v2 in range(v1 + 1, len(a1)):
                    v3 = a1[:v1] + a1[v1 + 1:v2] + a1[v2 + 1:]
                    v4, v5 = (a1[v1], a1[v2])
                    if possible(v3 + [v4 + v5]):
                        return True
                    if possible(v3 + [v4 * v5]):
                        return True
                    if possible(v3 + [v4 - v5]):
                        return True
                    if possible(v3 + [v5 - v4]):
                        return True
                    if v5 != 0 and possible(v3 + [v4 / v5]):
                        return True
                    if v4 != 0 and possible(v3 + [v5 / v4]):
                        return True
            return False
        return possible([Fraction(val) for v1 in a1])
