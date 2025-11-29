import itertools

class C1(object):

    def checkArithmeticSubarrays(self, a1, a2, a3):
        """
        """

        def is_arith(a1):
            v1, v2, v3 = (max(a1), min(a1), set(a1))
            if v1 == v2:
                return True
            v4, v5 = divmod(v1 - v2, len(a1) - 1)
            if v5:
                return False
            return all((i in v3 for v6 in range(v2, v1, v4)))
        v1 = []
        for v2, v3 in zip(a2, a3):
            v1.append(is_arith(a1[v2:v3 + 1]))
        return v1
