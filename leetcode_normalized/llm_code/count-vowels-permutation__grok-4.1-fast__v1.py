class C1:

    def countVowelPermutation(self, a1: int) -> int:
        v1 = 10 ** 9 + 7
        if a1 == 1:
            return 5
        v2 = [1] * 5
        for v3 in range(a1 - 1):
            v4 = [0] * 5
            v4[0] = (v2[1] + v2[2] + v2[4]) % v1
            v4[1] = (v2[0] + v2[2]) % v1
            v4[2] = (v2[1] + v2[3]) % v1
            v4[3] = v2[2] % v1
            v4[4] = (v2[2] + v2[3]) % v1
            v2 = v4
        return sum(v2) % v1
