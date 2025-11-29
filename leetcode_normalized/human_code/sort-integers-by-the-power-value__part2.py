class C1(object):
    v1 = {}

    def getKth(self, a1, a2, a3):
        """
        """

        def power_value(a1):
            v1, v2 = (a1, 0)
            while a1 > 1 and a1 not in C1.dp:
                v2 += 1
                if a1 % 2:
                    a1 = 3 * a1 + 1
                else:
                    a1 //= 2
            C1.dp[v1] = v2 + (C1.dp[a1] if a1 > 1 else 0)
            return (C1.dp[v1], v1)
        return sorted(list(range(a1, a2 + 1)), key=power_value)[a3 - 1]
