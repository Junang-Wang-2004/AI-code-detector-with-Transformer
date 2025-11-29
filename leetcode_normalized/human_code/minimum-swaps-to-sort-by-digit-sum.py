class C1(object):

    def minSwaps(self, a1):
        """
        """

        def total(a1):
            v1 = 0
            while a1:
                v1 += a1 % 10
                a1 //= 10
            return v1
        v1 = list(map(total, a1))
        v2 = list(range(len(a1)))
        v2.sort(key=lambda i: (v1[i], a1[i]))
        v3 = [-1] * len(v2)
        for v4, v5 in enumerate(v2):
            v3[v5] = v4
        v6 = 0
        v7 = [False] * len(a1)
        for v8 in range(len(a1)):
            v9 = 0
            while not v7[v8]:
                v7[v8] = True
                v9 += 1
                v8 = v3[v8]
            v6 += max(v9 - 1, 0)
        return v6
