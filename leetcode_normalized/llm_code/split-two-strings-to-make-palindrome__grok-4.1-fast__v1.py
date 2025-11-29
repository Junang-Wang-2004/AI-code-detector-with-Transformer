class C1:

    def checkPalindromeFormation(self, a1: str, a2: str) -> bool:

        def helper(a1: str, a2: str) -> bool:
            v1 = len(a1)
            v2 = 0
            while v2 < v1 - v2:
                if a1[v2] != a2[v1 - 1 - v2]:
                    break
                v2 += 1
            else:
                return True
            v3 = v1 - 1 - v2
            v4 = v2
            v5 = v3
            while v4 < v5:
                if a1[v4] != a1[v5]:
                    break
                v4 += 1
                v5 -= 1
            v6 = v4 >= v5
            v4 = v2
            v5 = v3
            while v4 < v5:
                if a2[v4] != a2[v5]:
                    break
                v4 += 1
                v5 -= 1
            v7 = v4 >= v5
            return v6 or v7
        return helper(a1, a2) or helper(a2, a1)
