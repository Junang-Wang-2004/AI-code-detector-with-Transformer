class C1(object):

    def maxSum(self, a1):
        v1 = [-1] * 10
        v2 = [-1] * 10

        def largest_digit(a1):
            if a1 == 0:
                return 0
            v1 = 0
            while a1 > 0:
                v1 = max(v1, a1 % 10)
                a1 //= 10
            return v1
        for v3 in a1:
            v4 = largest_digit(v3)
            if v1[v4] == -1 or v3 > v1[v4]:
                v2[v4] = v1[v4]
                v1[v4] = v3
            elif v2[v4] == -1 or v3 > v2[v4]:
                v2[v4] = v3
        v5 = -1
        for v6 in range(10):
            if v2[v6] != -1:
                v5 = max(v5, v1[v6] + v2[v6])
        return v5
