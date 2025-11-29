class C1:

    def numberOfUniqueGoodSubsequences(self, a1):
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = 0
        v4 = False
        for v5 in a1:
            v6 = (v2 + v3) % v1
            if v5 == '0':
                v2 = v6
                v4 = True
            else:
                v3 = (v6 + 1) % v1
        return (v2 + v3 + (1 if v4 else 0)) % v1
