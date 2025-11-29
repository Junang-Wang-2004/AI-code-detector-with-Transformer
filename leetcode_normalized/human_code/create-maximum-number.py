class C1(object):

    def maxNumber(self, a1, a2, a3):
        """
        """

        def get_max_digits(a1, a2, a3, a4):
            a4[a3] = max_digit(a1, a3)
            for v1 in reversed(range(a2, a3)):
                a4[v1] = delete_digit(a4[v1 + 1])

        def max_digit(a1, a2):
            v1 = len(a1) - a2
            v2 = []
            for v3 in a1:
                while v1 and v2 and (v2[-1] < v3):
                    v2.pop()
                    v1 -= 1
                v2.append(v3)
            return v2[:a2]

        def delete_digit(a1):
            v1 = list(a1)
            for v2 in range(len(v1)):
                if v2 == len(v1) - 1 or v1[v2] < v1[v2 + 1]:
                    v1 = v1[:v2] + v1[v2 + 1:]
                    break
            return v1

        def merge(a1, a2):
            return [max(a1, a2).pop(0) for v1 in range(len(a1) + len(a2))]
        v1, v2 = (len(a1), len(a2))
        v3, v4 = ([[] for v5 in range(a3 + 1)], [[] for v5 in range(a3 + 1)])
        get_max_digits(a1, max(0, a3 - v2), min(a3, v1), v3)
        get_max_digits(a2, max(0, a3 - v1), min(a3, v2), v4)
        return max((merge(v3[i], v4[a3 - i]) for v6 in range(max(0, a3 - v2), min(a3, v1) + 1)))
