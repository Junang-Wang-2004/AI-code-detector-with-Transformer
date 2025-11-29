v1 = 10 ** 4
v2 = [-1] * v1

class C1(object):

    def countSymmetricIntegers(self, a1, a2):
        """
        """

        def check(a1):
            if v2[a1 - 1] == -1:
                v1 = list(map(int, str(a1)))
                if len(v1) % 2:
                    v2[a1 - 1] = 0
                else:
                    v2[a1 - 1] = int(sum((v1[i] for v2 in range(len(v1) // 2))) == sum((v1[v2] for v2 in range(len(v1) // 2, len(v1)))))
            return v2[a1 - 1]
        return sum((check(x) for v1 in range(a1, a2 + 1)))
